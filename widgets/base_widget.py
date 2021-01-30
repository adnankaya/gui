import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame


class BaseWidget(ttk.Panedwindow):
    def __init__(self, master=None, **kw):
        ttk.Panedwindow.__init__(self, master, **kw)
        self.F_Buttons = ttk.Frame(self)
        self.btn_save = tk.Button(self.F_Buttons)
        self.btn_save.configure(activebackground='#404040', activeforeground='#ffffff', background='#404040', cursor='hand2')
        self.btn_save.configure(font='{verdana} 12 {bold}', foreground='#ffffff', text='Save')
        self.btn_save.pack(padx='5', pady='5', side='left')
        self.btn_save.configure(command=self.save)
        self.btn_start = tk.Button(self.F_Buttons)
        self.btn_start.configure(activebackground='#336699', activeforeground='#ffffff', background='#336699', font='{verdana} 12 {bold}')
        self.btn_start.configure(foreground='#ffffff', text='Start')
        self.btn_start.pack(side='left')
        self.btn_start.configure(command=self.start)
        self.btn_stop = tk.Button(self.F_Buttons)
        self.btn_stop.configure(activebackground='#ff0011', activeforeground='#ffffff', background='#ff0011', font='{verdana} 12 {bold}')
        self.btn_stop.configure(foreground='#ffffff', text='Stop')
        self.btn_stop.pack(side='left')
        self.btn_stop.configure(command=self.stop)
        self.btn_histogram = tk.Button(self.F_Buttons)
        self.btn_histogram.configure(font='{verdana} 12 {bold}', text='Histogram')
        self.btn_histogram.pack(side='left')
        self.btn_histogram.configure(command=self.histogram)
        self.F_Resize = ttk.Frame(self.F_Buttons)
        self.lb_resize = ttk.Label(self.F_Resize)
        self.lb_resize.configure(text='Resize')
        self.lb_resize.pack(padx='5', pady='5', side='left')
        self.scale_resize = ttk.Scale(self.F_Resize)
        self.scale_resize.configure(from_='20', orient='horizontal', to='100')
        self.scale_resize.pack(padx='5', pady='5', side='left')
        self.scale_resize.bind('<B1-Motion>', self.get_resize_val, add='')
        self.lb_resize_res = ttk.Label(self.F_Resize)
        self.lb_resize_res.configure(text='0')
        self.lb_resize_res.pack(padx='5', pady='5', side='right')
        self.F_Resize.configure(height='200', relief='groove', width='200')
        self.F_Resize.pack(padx='10', pady='10', side='top')
        self.F_Buttons.configure(height='200', relief='groove', width='200')
        self.F_Buttons.pack(side='top')
        self.add(self.F_Buttons, weight='1')
        self.panedwindow_2 = ttk.Panedwindow(self, orient='horizontal')
        self.SF_Canvas = ScrolledFrame(self.panedwindow_2, scrolltype='both')
        self.canvas_image = tk.Canvas(self.SF_Canvas.innerframe)
        self.canvas_image.configure(background='#6961b8', height='480', width='640')
        self.canvas_image.pack(expand='true', fill='both', side='top')
        self.SF_Canvas.configure(usemousewheel=False)
        self.SF_Canvas.pack(expand='true', fill='both', side='top')
        self.panedwindow_2.add(self.SF_Canvas, weight='1')
        self.SF_Toolbar = ScrolledFrame(self.panedwindow_2, scrolltype='both')
        self.F_Thresh = ttk.Frame(self.SF_Toolbar.innerframe)
        self.cb_adjusted = tk.Checkbutton(self.F_Thresh)
        self.cb_adjusted.configure(font='{verdana} 10 {}', text='Adjusted')
        self.cb_adjusted.pack(anchor='nw', pady='5', side='top')
        self.lb_thresh = ttk.Label(self.F_Thresh)
        self.lb_thresh.configure(text='Threshold')
        self.lb_thresh.pack(padx='5', pady='5', side='left')
        self.scale_thresh = ttk.Scale(self.F_Thresh)
        self.scale_thresh.configure(from_='0', length='150', orient='horizontal', to='100')
        self.scale_thresh.pack(padx='5', pady='5', side='left')
        self.scale_thresh.bind('<B1-Motion>', self.get_thresh_val, add='')
        self.lb_thresh_res = ttk.Label(self.F_Thresh)
        self.lb_thresh_res.configure(text='0')
        self.lb_thresh_res.pack(padx='5', pady='5', side='right')
        self.F_Thresh.configure(height='200', relief='groove', width='200')
        self.F_Thresh.pack(pady='10', side='top')
        self.F_Colorspace = ttk.Frame(self.SF_Toolbar.innerframe)
        self.lb_colorspace = ttk.Label(self.F_Colorspace)
        self.lb_colorspace.configure(text='Colorspace')
        self.lb_colorspace.pack(side='left')
        self.combo_colorspace = ttk.Combobox(self.F_Colorspace)
        self.combo_colorspace.configure(cursor='hand2', state='readonly', width='20')
        self.combo_colorspace.pack(side='left')
        self.combo_colorspace.bind('<<ComboboxSelected>>', self.select_colorspace, add='')
        self.F_Colorspace.configure(height='200', width='200')
        self.F_Colorspace.pack(side='top')
        self.SF_Toolbar.configure(usemousewheel=False)
        self.SF_Toolbar.pack(side='top')
        self.panedwindow_2.add(self.SF_Toolbar, weight='1')
        self.panedwindow_2.configure(height='200', width='200')
        self.panedwindow_2.pack(side='top')
        self.add(self.panedwindow_2, weight='12')
        self.NB_Footer = ttk.Notebook(self)
        self.txt_log = tk.Text(self.NB_Footer)
        self.txt_log.configure(background='#404040', foreground='#ffffff', height='10', width='50')
        _text_ = '''text_1'''
        self.txt_log.insert('0.0', _text_)
        self.txt_log.pack(side='top')
        self.NB_Footer.add(self.txt_log, text='Message Log')
        self.F_Live_Hist = ttk.Frame(self.NB_Footer)
        self.F_Live_Hist.configure(height='200', width='200')
        self.F_Live_Hist.pack(side='top')
        self.NB_Footer.add(self.F_Live_Hist, text='Live Histogram')
        self.NB_Footer.configure(height='200', width='200')
        self.NB_Footer.pack(side='top')
        self.add(self.NB_Footer, weight='1')

    def save(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def histogram(self):
        pass

    def get_resize_val(self, event=None):
        pass

    def get_thresh_val(self, event=None):
        pass

    def select_colorspace(self, event=None):
        pass



