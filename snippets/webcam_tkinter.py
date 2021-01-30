# pip install Pillow opencv-python numpy
import tkinter as tk
import cv2 as cv
import PIL.Image
import PIL.ImageTk


root = tk.Tk()

CAM_ADRESSES = ["/dev/video0", "/dev/video1", "/dev/video2"]

camera = cv.VideoCapture(CAM_ADRESSES[0])

lbimage = tk.Label()
lbimage.pack(side="top", anchor="center",expand=True, fill="both")

def capture():
    try:
        res, frame = camera.read()
        if res:
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            lbimage.imgtk = img
            lbimage.configure(image=img)
            root.after(1, capture)
    except Exception as exc:
        print(f"Hata: {exc}")


root.geometry("800x600")
root.after(1000, capture)
root.mainloop()
