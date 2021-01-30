import tkinter as tk
import tkinter.ttk as ttk

class Header(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        lb = ttk.Label(text="Header")
        lb.pack()

class Body(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        btn = tk.Button(master, text='Body Button')
        btn.pack()

class Footer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        cb = ttk.Checkbutton(master, text='Onaylıyorum!')
        cb.pack()


class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        Header(master).pack(side='top',pady="100")
        Body(master).pack(side='top',pady="100")
        Footer(master).pack(side='bottom',pady="100")

        master.mainloop()

class Application:
    window = tk.Tk()
    window.geometry("800x600")
    main = Main(window)

