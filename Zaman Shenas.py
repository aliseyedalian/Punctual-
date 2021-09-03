import tkinter as tk
from tkinter import Label,Entry, messagebox as mb
import threading


def letsgo():  
    try:
        min = int(entryMin.get())        
    except ValueError:
        mb.showerror(title="خطا", message= "مقدار ورودی نادرست است")
    sec = min * 60
    global timer
    timer = threading.Timer(sec, finish)
    timer.start()
    global setTimer
    setTimer = True
    switch()

def switch():
    if letsgoBtn["state"] == "normal":
        letsgoBtn["state"] = "disabled"
        entryMin["state"] = "disabled"
    else:
        letsgoBtn["state"] = "normal"
        entryMin["state"] = "normal"

def finish():
    mb.showinfo(title='اتمام زمان',message='خدا قوت، کمی استراحت کنید')
    switch()
                
def onClose():
    if mb.askokcancel(title="خروج", message="می خواهید از برنامه زمان شناس خارج شوید؟"):
        if(setTimer):
            timer.cancel()
        root.destroy()

def main():
    global setTimer
    setTimer = False
    global root
    root= tk.Tk()
    root.title('زمان شناس')
    canvas = tk.Canvas(root, width = 400, height = 300)
    canvas.pack()
    questionLabel = Label(root, text= 'چند دقیقه می خواهید با سیستم کار کنید؟')
    canvas.create_window(200, 100, window=questionLabel)
    global entryMin
    entryMin = Entry (root) 
    canvas.create_window(200, 140, window=entryMin)
    global letsgoBtn
    letsgoBtn = tk.Button(text='بزن بریم', command=letsgo)
    canvas.create_window(200, 180, window=letsgoBtn)
    root.protocol("WM_DELETE_WINDOW", onClose)
    root.mainloop()

if __name__ == '__main__':
    main()