import tkinter as tk

class Window1:
    def __init__(self, master):
        self.master=master
        btn = tk.Button(text="2.Pencere",command=self.open_win2)
        btn.pack()

    def open_win2(self):
        self.toplevel = tk.Toplevel(self.master)
        self.toplevel.geometry("300x300")
        self.win2 = Window2(self.toplevel)
        
class Window2:
    def __init__(self, master):
        self.master = master
        btn = tk.Button(self.master,text="Kapat",command=self.close)
        btn.pack(pady="50")
    
    def close(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    win1 = Window1(root)
    root.mainloop()