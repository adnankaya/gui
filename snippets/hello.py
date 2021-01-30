import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
import os
from PIL import Image, ImageTk

BASEDIR = os.path.dirname(os.path.abspath(__file__))
window = tk.Tk()

filename = f"{BASEDIR}/ac.jpeg"
canvas1 = tk.Canvas(window)
canvas1.pack(side="top", anchor="center")
img = ImageTk.PhotoImage(image=Image.open(filename))
canvas1.create_image(0,0,image=img,anchor='center')


def browse():
    file = askopenfile(
        initialdir=BASEDIR,
        title='Dosya seçin',
        filetypes=(
            ("all types","*.*"),
            ("Text files","*.txt")
        )
    )

    print(f"secilen dosya: {file.name}")

btnbrowse = tk.Button(window, text='Browse', command=browse)
btnbrowse.pack(side='left', anchor='nw', padx='20', pady='20')

def on_selected_country(event=None):
    print(f"seçilen ulke: {com1.get()}")

countries = ['Turkey','Palestine','East Turkistan', 'Chechenya']
com1 = ttk.Combobox(window, values=countries, state='readonly')
com1.set(countries[0])
com1.bind('<<ComboboxSelected>>', func=on_selected_country)
com1.pack(side='top', pady='20')

def get_scale_var(event=None):
    print(s1var.get())

s1var = tk.IntVar(window)
s1 = tk.Scale(window, variable=s1var, orient='horizontal', from_=20, to=180)
s1.bind('<B1-Motion>', func=get_scale_var)
s1.pack(side='top', pady='20')

cb1var = tk.BooleanVar(window)
cb1 = tk.Checkbutton(window, text="Onaylıyorum!", variable=cb1var)
cb1.pack(side="bottom", pady="10")

mystr = tk.StringVar(window)
msg = tk.Entry(window, textvariable=mystr)
msg.pack(side="left", anchor="ne")

lb1 = tk.Label(window, text="İlk Mesaj")
lb1.pack(side="left", anchor="n")

def on_click():
    print(f"onaylandı mı ? : {cb1var.get()}")
    lb1.config(text=mystr.get())

btn = tk.Button(window, text="Tıkla", command=on_click)
btn.pack(side="right", anchor="n")


window.geometry("800x600")
window.mainloop()