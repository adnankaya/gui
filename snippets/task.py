import tkinter as tk
window = tk.Tk()

counter = 0
print("start window")
def task():
    global counter
    counter +=1 
    lb.config(text=f"Sayaç! {counter}")
    print("task() works...")
    window.after(2000,task)

lb = tk.Label(text=f"Sayaç: {counter}")
lb.config(font='{Verdana} 30 {}',)
lb.pack(pady='50')

window.geometry("400x300")
window.config(background='#fcba03')
print("started mainloop --------")
window.after(1500, task)
window.mainloop()
print("-------- end mainloop")