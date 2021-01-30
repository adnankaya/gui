import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

lb = tk.Label(text="Türkçe Tkinter Dersleri")
lb2 = tk.Label(text="İngilizce Tkinter Dersleri")
# lb.pack(side='left')
# lb.place(x=20, y=100)
lb.grid(row=0,column=0)
lb2.grid(row=1,column=0)

def on_click():
    lb.config(text='Merhaba :)')

btn = tk.Button(window, text="Tıkla", command=on_click)
btn2 = tk.Button(window, text="Click", command=on_click)
# btn.pack(side='left')
# btn.place(x=300, y=20)
btn.grid(row=0, column=1)
btn2.grid(row=1, column=1)

window.geometry("400x300")
window.mainloop()