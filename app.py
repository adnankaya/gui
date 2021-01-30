import tkinter as tk
import tkinter.ttk as ttk

# internals 
from widgets.base import Base

class Application():
    def __init__(self, master):
        style_global = ttk.Style()
        style_global.theme_use('clam')

        base = Base(master)
        base.pack(expand=True, fill='both')

        master.mainloop()


if __name__=='__main__':
    window = tk.Tk()
    window.geometry("1000x600")
    window.title("Kayace | Tkinter Dersleri")
    app = Application(window)
