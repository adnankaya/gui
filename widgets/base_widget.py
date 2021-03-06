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
        self.scale_resize.configure(from_='20', length='200', orient='horizontal', to='100')
        self.scale_resize.pack(padx='5', pady='5', side='left')
        self.scale_resize.bind('<B1-Motion>', self.get_resize_val, add='')
        self.lb_resize_res = ttk.Label(self.F_Resize)
        self.lb_resize_res.configure(text='0')
        self.lb_resize_res.pack(padx='5', pady='5', side='right')
        self.F_Resize.configure(height='200', relief='groove', width='200')
        self.F_Resize.pack(padx='10', pady='10', side='left')
        self.cb_adjusted = tk.Checkbutton(self.F_Buttons)
        self.cb_adjusted.configure(font='{verdana} 10 {}', text='Adjusted')
        self.cb_adjusted.pack(pady='5', side='left')
        self.F_Buttons.configure(height='200', relief='groove', width='200')
        self.F_Buttons.pack(side='top')
        self.add(self.F_Buttons, weight='1')
        self.PW_Body = ttk.Panedwindow(self, orient='horizontal')
        self.SF_Canvas = ScrolledFrame(self.PW_Body, scrolltype='both')
        self.canvas_image = tk.Canvas(self.SF_Canvas.innerframe)
        self.canvas_image.configure(background='#2c2c2c', height='480', width='640')
        self.canvas_image.pack(expand='true', fill='both', side='top')
        self.SF_Canvas.configure(usemousewheel=False)
        self.SF_Canvas.pack(expand='true', fill='both', side='top')
        self.PW_Body.add(self.SF_Canvas, weight='3')
        self.SF_Toolbar = ScrolledFrame(self.PW_Body, scrolltype='both')
        self.F_Colorspace = ttk.Frame(self.SF_Toolbar.innerframe)
        self.lb_colorspace = ttk.Label(self.F_Colorspace)
        self.lb_colorspace.configure(text='Colorspace')
        self.lb_colorspace.pack(anchor='nw', padx='5', pady='5', side='left')
        self.combo_colorspace = ttk.Combobox(self.F_Colorspace)
        self.combo_colorspace.configure(cursor='hand2', state='readonly', width='8')
        self.combo_colorspace.pack(anchor='nw', padx='5', pady='5', side='left')
        self.combo_colorspace.bind('<<ComboboxSelected>>', self.select_colorspace, add='')
        self.cbch1 = tk.Checkbutton(self.F_Colorspace)
        self.cbch1.configure(cursor='hand2', text='c1')
        self.cbch1.pack(anchor='center', padx='5', pady='5', side='left')
        self.cbch2 = tk.Checkbutton(self.F_Colorspace)
        self.cbch2.configure(cursor='hand2', text='c2')
        self.cbch2.pack(anchor='center', padx='5', pady='5', side='left')
        self.cbch3 = tk.Checkbutton(self.F_Colorspace)
        self.cbch3.configure(cursor='hand2', text='c3')
        self.cbch3.pack(anchor='center', padx='5', pady='5', side='left')
        self.F_Colorspace.configure(height='200', relief='groove', width='200')
        self.F_Colorspace.pack(fill='x', pady='5', side='top')
        self.F_Thresh = ttk.Frame(self.SF_Toolbar.innerframe)
        self.combobox_threshtype = ttk.Combobox(self.F_Thresh)
        self.combobox_threshtype.configure(cursor='hand2', state='readonly', width='20')
        self.combobox_threshtype.pack(anchor='nw', padx='5', pady='5', side='top')
        self.combobox_threshtype.bind('<<ComboboxSelected>>', self.select_thresh_type, add='')
        self.lb_thresh = ttk.Label(self.F_Thresh)
        self.lb_thresh.configure(text='Threshold')
        self.lb_thresh.pack(padx='5', pady='5', side='left')
        self.scale_thresh = ttk.Scale(self.F_Thresh)
        self.scale_thresh.configure(from_='0', length='200', orient='horizontal', to='255')
        self.scale_thresh.pack(padx='5', pady='5', side='left')
        self.scale_thresh.bind('<B1-Motion>', self.get_thresh_val, add='')
        self.lb_thresh_res = ttk.Label(self.F_Thresh)
        self.lb_thresh_res.configure(text='0')
        self.lb_thresh_res.pack(padx='5', pady='5', side='right')
        self.F_Thresh.configure(height='200', relief='groove', width='200')
        self.F_Thresh.pack(fill='x', side='top')
        self.F_Contrast = ttk.Frame(self.SF_Toolbar.innerframe)
        self.lb_contrast = ttk.Label(self.F_Contrast)
        self.lb_contrast.configure(text='Contrast')
        self.lb_contrast.pack(padx='5', pady='5', side='left')
        self.scale_contrast = ttk.Scale(self.F_Contrast)
        self.scale_contrast.configure(cursor='hand2', from_='0', length='200', orient='horizontal')
        self.scale_contrast.configure(to='30')
        self.scale_contrast.pack(padx='5', pady='5', side='left')
        self.scale_contrast.bind('<B1-Motion>', self.get_contrast, add='')
        self.lb_contrast_res = ttk.Label(self.F_Contrast)
        self.lb_contrast_res.configure(text='0')
        self.lb_contrast_res.pack(padx='5', pady='5', side='right')
        self.F_Contrast.configure(height='200', relief='groove', width='200')
        self.F_Contrast.pack(fill='x', side='top')
        self.F_Bright = ttk.Frame(self.SF_Toolbar.innerframe)
        self.lb_bright = ttk.Label(self.F_Bright)
        self.lb_bright.configure(text='Brightness')
        self.lb_bright.pack(padx='5', pady='5', side='left')
        self.scale_bright = ttk.Scale(self.F_Bright)
        self.scale_bright.configure(cursor='hand2', from_='-127', length='200', orient='horizontal')
        self.scale_bright.configure(to='127')
        self.scale_bright.pack(padx='5', pady='5', side='left')
        self.scale_bright.bind('<B1-Motion>', self.get_bright, add='')
        self.lb_bright_res = ttk.Label(self.F_Bright)
        self.lb_bright_res.configure(text='0')
        self.lb_bright_res.pack(padx='5', pady='5', side='right')
        self.F_Bright.configure(height='200', relief='groove', width='200')
        self.F_Bright.pack(fill='x', pady='5', side='top')
        self.F_Morph = ttk.Frame(self.SF_Toolbar.innerframe)
        self.lb_morph = ttk.Label(self.F_Morph)
        self.lb_morph.configure(text='Morph.')
        self.lb_morph.pack(padx='5', pady='5', side='left')
        self.combobox_morph = ttk.Combobox(self.F_Morph)
        self.combobox_morph.configure(state='readonly', width='12')
        self.combobox_morph.pack(padx='5', pady='5', side='left')
        self.combobox_morph.bind('<<ComboboxSelected>>', self.select_morph, add='')
        self.lb_morph_kernel = ttk.Label(self.F_Morph)
        self.lb_morph_kernel.configure(text='Kernel')
        self.lb_morph_kernel.pack(padx='5', pady='5', side='left')
        self.spin_kernel = ttk.Spinbox(self.F_Morph)
        self.spin_kernel.configure(cursor='hand2', font='{verdana} 12 {}', from_='1', to='20')
        self.spin_kernel.configure(width='6')
        _text_ = '''1'''
        self.spin_kernel.delete('0', 'end')
        self.spin_kernel.insert('0', _text_)
        self.spin_kernel.pack(padx='5', pady='5', side='left')
        self.F_Morph.configure(height='200', relief='groove', width='200')
        self.F_Morph.pack(fill='x', side='top')
        self.F_Hist_Eq = ttk.Frame(self.SF_Toolbar.innerframe)
        self.cb_hist_eq = tk.Checkbutton(self.F_Hist_Eq)
        self.cb_hist_eq.configure(cursor='hand2', text='Histogram Equalization')
        self.cb_hist_eq.pack(padx='5', pady='5', side='left')
        self.F_Hist_Eq.configure(height='200', relief='groove', width='200')
        self.F_Hist_Eq.pack(fill='x', pady='5', side='top')
        self.F_Clahe = ttk.Frame(self.SF_Toolbar.innerframe)
        self.cb_clahe = tk.Checkbutton(self.F_Clahe)
        self.cb_clahe.configure(cursor='hand2', text='Clahe')
        self.cb_clahe.pack(anchor='nw', padx='5', pady='5', side='top')
        self.lbCL = ttk.Label(self.F_Clahe)
        self.lbCL.configure(text='ClipLimit')
        self.lbCL.pack(padx='5', pady='5', side='left')
        self.spin_cliplimit = ttk.Spinbox(self.F_Clahe)
        self.spin_cliplimit.configure(cursor='hand2', from_='1', to='255', width='4')
        _text_ = '''1'''
        self.spin_cliplimit.delete('0', 'end')
        self.spin_cliplimit.insert('0', _text_)
        self.spin_cliplimit.pack(padx='5', pady='5', side='left')
        self.lbTileGS = ttk.Label(self.F_Clahe)
        self.lbTileGS.configure(text='TileGridSize')
        self.lbTileGS.pack(padx='5', pady='5', side='left')
        self.spin_tgs = ttk.Spinbox(self.F_Clahe)
        self.spin_tgs.configure(cursor='hand2', from_='1', to='100', width='4')
        _text_ = '''1'''
        self.spin_tgs.delete('0', 'end')
        self.spin_tgs.insert('0', _text_)
        self.spin_tgs.pack(side='left')
        self.F_Clahe.configure(height='200', relief='groove', width='200')
        self.F_Clahe.pack(fill='x', side='top')
        self.SF_Toolbar.configure(usemousewheel=False)
        self.SF_Toolbar.pack(side='top')
        self.PW_Body.add(self.SF_Toolbar, weight='1')
        self.PW_Body.configure(height='200', width='200')
        self.PW_Body.pack(side='top')
        self.add(self.PW_Body, weight='16')
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

    def select_colorspace(self, event=None):
        pass

    def select_thresh_type(self, event=None):
        pass

    def get_thresh_val(self, event=None):
        pass

    def get_contrast(self, event=None):
        pass

    def get_bright(self, event=None):
        pass

    def select_morph(self, event=None):
        pass



