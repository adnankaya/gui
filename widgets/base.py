import tkinter as tk
import tkinter.ttk as ttk
import PIL.Image
import PIL.ImageTk
import cv2 as cv
import numpy as np
# internals
from .base_widget import BaseWidget
from camera import Camera


class Base(BaseWidget):
    def __init__(self, *args, **kwargs):
        BaseWidget.__init__(self, *args, **kwargs)
        self.miliseconds = 1
        # Checkboxes
        self.cb_adjusted_var = tk.BooleanVar(self.F_Buttons)
        self.cb_adjusted.configure(variable=self.cb_adjusted_var)
        self.cb_hist_eq_var = tk.BooleanVar(self.F_Hist_Eq)
        self.cb_hist_eq.configure(variable=self.cb_hist_eq_var)
        self.cb_clahe_var = tk.BooleanVar(self.F_Clahe)
        self.cb_clahe.configure(variable=self.cb_clahe_var)

        # Scales
        self.scale_thresh_var = tk.IntVar(self.F_Thresh, value=0)
        self.scale_thresh.configure(variable=self.scale_thresh_var)
        self.lb_thresh_res['text'] = str(self.scale_thresh_var.get())

        self.scale_resize_var = tk.IntVar(self.F_Resize, value=60)
        self.scale_resize.configure(variable=self.scale_resize_var)
        self.lb_resize_res['text'] = str(self.scale_resize_var.get())

        self.scale_contrast_var = tk.IntVar(self.F_Contrast, value=10)
        self.scale_contrast.configure(variable=self.scale_contrast_var)
        self.lb_contrast_res['text'] = str(self.scale_contrast_var.get()/10)

        self.scale_bright_var = tk.IntVar(self.F_Bright, value=0)
        self.scale_bright.configure(variable=self.scale_bright_var)
        self.lb_bright_res['text'] = str(self.scale_bright_var.get())

        colorspaces = ['None', 'RGB', 'Gray', 'HSV', 'CIELab']
        self.combo_colorspace.configure(values=colorspaces)
        self.combo_colorspace.set(colorspaces[0])

        morph_list = ['None', 'erosion', 'dilation',
                      'opening', 'closing', 'gradient',
                      'top hat', 'black hat']
        self.combobox_morph.configure(values=morph_list)
        self.combobox_morph.set(morph_list[0])

        THRESH_TYPES = ['None', 'BINARY', 'BINARY_INV',
                        'TRUNC', 'TOZERO', 'TOZERO_INV']
        self.combobox_threshtype.configure(values=THRESH_TYPES)
        self.combobox_threshtype.set(THRESH_TYPES[0])

        # spinbox
        style_spin = ttk.Style()
        style_spin.configure("TSpinbox", arrowsize=20, arrowcolor="#336699")
        self.spin_kernel.config(style='TSpinbox')

    def start(self):
        try:
            self.camera = Camera(camera_source='/dev/video0')
            self.capture()
        except Exception as exc:
            self.txt_log.insert('0.0', f"{exc}")

    def capture(self):
        try:
            frame = self.camera.get_origin_frames()
            if frame is not None:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

                if self.cb_adjusted_var.get():                
                    if self.combo_colorspace.get():
                        frame = self.get_frame_by_colorspace(frame)

                    if self.get_contrast() != 1 and self.get_bright() != 0:
                        frame = self.apply_contrast_brightness_to_frame(frame)

                    if self.get_thresh_val() != 0 and self.combobox_threshtype.get() != 'None':
                        frame = self.get_thresholded_frame(frame)
                    
                    if self.combo_colorspace.get()=='Gray' and self.combobox_morph.get()!='None':
                        frame = self.apply_morphology(frame)

                resizedframe = self.camera.resize_frame(
                    img=frame, scale_percent=self.get_resize_val()
                )

                self.canvasframe = PIL.ImageTk.PhotoImage(
                    image=PIL.Image.fromarray(resizedframe))
                self.canvas_image.create_image(
                    0, 0, image=self.canvasframe, anchor="nw")
                self.after(self.miliseconds, self.capture)

        except Exception as exc:
            self.txt_log.insert('0.0', f"{exc}")

    def get_frame_by_colorspace(self, frame):
        val = self.combo_colorspace.get()
        if val == 'Gray':
            frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        if val == 'HSV':
            frame = cv.cvtColor(frame, cv.COLOR_RGB2HSV)
        if val == 'CIELab':
            frame = cv.cvtColor(frame, cv.COLOR_RGB2LAB)

        return frame

    def get_resize_val(self, event=None):
        val = self.scale_resize_var.get()
        self.lb_resize_res['text'] = str(val)
        return val

    def get_thresh_val(self, event=None):
        val = self.scale_thresh_var.get()
        self.lb_thresh_res['text'] = str(val)
        return val

    def select_colorspace(self, event=None):
        val = self.combo_colorspace.get()
        print(type(val), val)

    def get_thresholded_frame(self, frame):
        val = self.combobox_threshtype.get()
        maxval = 255
        thresh = self.get_thresh_val()
        if val == 'BINARY':
            r, frame = cv.threshold(frame, thresh, maxval, cv.THRESH_BINARY)
        if val == 'BINARY_INV':
            r, frame = cv.threshold(
                frame, thresh, maxval, cv.THRESH_BINARY_INV)
        if val == 'TOZERO':
            r, frame = cv.threshold(frame, thresh, maxval, cv.THRESH_TOZERO)
        if val == 'TOZERO_INV':
            r, frame = cv.threshold(
                frame, thresh, maxval, cv.THRESH_TOZERO_INV)
        if val == 'TRUNC':
            r, frame = cv.threshold(frame, thresh, maxval, cv.THRESH_TRUNC)
        return frame

    def apply_morphology(self, frame):
        spinvar = int(self.spin_kernel.get())
        kernel = np.ones((spinvar, spinvar), np.uint8)
        val = self.combobox_morph.get()
        if val == 'erosion':
            frame = cv.erode(frame, kernel)
        if val == 'dilation':
            frame = cv.dilate(frame, kernel)
        if val == 'opening':
            frame = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
        if val == 'closing':
            frame = cv.morphologyEx(frame, cv.MORPH_CLOSE, kernel)
        if val == 'gradient':
            frame = cv.morphologyEx(frame, cv.MORPH_GRADIENT, kernel)
        if val == 'top hat':
            frame = cv.morphologyEx(frame, cv.MORPH_TOPHAT, kernel)
        if val == 'black hat':
            frame = cv.morphologyEx(frame, cv.MORPH_BLACKHAT, kernel)
        return frame

    def get_contrast(self, event=None):
        val = int(self.scale_contrast.get()) / 10
        self.lb_contrast_res['text'] = str(val)
        return val

    def get_bright(self, event=None):
        val = int(self.scale_bright.get())
        self.lb_bright_res['text'] = str(val)
        return val

    def apply_contrast_brightness_to_frame(self, frame):
        alpha = float(self.get_contrast())
        beta = float(self.get_bright())
        contrasted = cv.convertScaleAbs(frame, alpha=alpha, beta=beta)
        return contrasted
