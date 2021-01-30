import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

btn_save = tk.Button(text='Save')
btn_save.pack(anchor='center', side='top', pady="10")
btn_save.config(cursor='hand2', font='{Verdana} 10 {}', foreground='#ffffff')
btn_save.config(activebackground='red', 
activeforeground='green', 
background='#232323', borderwidth='2')

style1 = ttk.Style()
style1.configure('TLabel', background='black', foreground='green', padding="10")

lb = ttk.Label(text="Adnan Kaya")
lb.pack(pady=20)

style1.configure('TButton', 
    background='#336699', 
    foreground='black', 
    highlightthickness='20',
    font=('Helvetica', 18, 'bold')
)

btn1 = ttk.Button(text='Buton1', style='TButton')
btn1.pack()

style1.map('asd.TButton',
        foreground=[('disabled', 'yellow'),
                    ('pressed', 'red'),
                    ('active', 'blue')],
        background=[('disabled', 'magenta'),
                    ('pressed', '!focus', 'cyan'),
                    ('active', 'green')],
        highlightcolor=[('focus', 'green'),
                        ('!focus', 'red')],
        relief=[('pressed', 'groove'),
                ('!pressed', 'ridge')])
btn2 = ttk.Button(text='Buton2', style="asd.TButton")
btn2.pack()

window.geometry("400x300")
window.config(background="#404040")
window.mainloop()
