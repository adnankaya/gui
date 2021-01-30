import tkinter as tk
import tkinter.ttk as ttk
import PIL.Image
import PIL.ImageTk
import cv2 as cv
# internals
from .base_widget import BaseWidget
from camera import Camera


class Base(BaseWidget):
    def __init__(self, *args, **kwargs):
        BaseWidget.__init__(self, *args, **kwargs)
        self.miliseconds = 1
        # Checkboxes
        self.cb_adjusted_var = tk.BooleanVar(self.F_Thresh)
        self.cb_adjusted.configure(variable=self.cb_adjusted_var)
        self.cb_hist_eq_var = tk.BooleanVar(self.F_Hist_Eq)
        self.cb_hist_eq.configure(variable=self.cb_hist_eq_var)
        self.cb_clahe_var = tk.BooleanVar(self.F_Clahe)
        self.cb_clahe.configure(variable=self.cb_clahe_var)
        
        # Scales
        self.scale_thresh_var = tk.IntVar(self.F_Thresh, value=20)
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

        colorspaces = ['None','RGB', 'Gray', 'HSV', 'CIELab']
        self.combo_colorspace.configure(values=colorspaces)
        self.combo_colorspace.set(colorspaces[0])

        morph_list = ['None', 'erosion', 'dilation',
                'opening', 'closing', 'gradient',
                'top hat', 'black hat']
        self.combobox_morph.configure(values=morph_list)
        self.combobox_morph.set(morph_list[0])

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

                if self.combo_colorspace.get():
                    frame = self.get_frame_by_colorspace(frame)
                
                if self.get_contrast()!= 1 and self.get_bright()!=0:
                    frame = self.apply_contrast_brightness_to_frame(frame)

                resizedframe = self.camera.resize_frame(
                    img=frame, scale_percent=self.get_resize_val()
                )

                self.canvasframe = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(resizedframe))
                self.canvas_image.create_image(0,0,image=self.canvasframe,anchor="nw")
                self.after(self.miliseconds, self.capture)

        except Exception as exc:
            self.txt_log.insert('0.0',f"{exc}")

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

    def select_colorspace(self, event=None):
        val = self.combo_colorspace.get()
        print(type(val), val)

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