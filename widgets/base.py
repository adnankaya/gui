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

        self.cb_adjusted_var = tk.BooleanVar(self.F_Thresh)
        self.cb_adjusted.configure(variable=self.cb_adjusted_var)

        self.scale_thresh_var = tk.IntVar(self.F_Thresh, value=20)
        self.scale_thresh.configure(variable=self.scale_thresh_var)
        self.lb_thresh_res['text'] = str(self.scale_thresh_var.get())

        self.scale_resize_var = tk.IntVar(self.F_Resize, value=20)
        self.scale_resize.configure(variable=self.scale_resize_var)
        self.lb_resize_res['text'] = str(self.scale_resize_var.get())

        colorspaces = ['BGR', 'Gray', 'HSV', 'CIELab']
        self.combo_colorspace.configure(values=colorspaces)

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
