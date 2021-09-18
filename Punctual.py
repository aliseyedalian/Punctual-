from tkinter import *
from tkinter import Label,Entry, messagebox as mb
import threading

def main():
    global isRunning
    isRunning = False
    global root
    root = Tk(className='Punctual')
    root.iconbitmap('icon/icon.ico')
    canvas = Canvas(root, width = 400, height = 150)
    canvas.pack()
    questionLabel = Label(root, text= 'How many minutes do you want to work with the system?')
    canvas.create_window(200, 20, window=questionLabel)
    global entryMin
    entryMin = Entry (root) 
    canvas.create_window(200, 50, window=entryMin, width=100)
    global letsgoBtn
    letsgoBtn = Button(text='Let\'s go!', command=letsgo)
    canvas.create_window(200, 80, window=letsgoBtn,  width=100)
    global stopBtn
    stopBtn = Button(text='Stop it!', command=stop)
    canvas.create_window(200, 110, window=stopBtn, width=100)
    stopBtn["state"] = "disabled"
    root.protocol("WM_DELETE_WINDOW", onClose)
    root.mainloop()

def letsgo():  
    try:
        min = int(entryMin.get())        
    except ValueError:
        mb.showerror(title="Error", message= "Unvalid Input!")
    sec = min #* 60
    global timer
    timer = threading.Timer(sec, finish)
    timer.start()
    global isRunning
    isRunning = True
    switch()

def stop():
    global isRunning
    if(isRunning):
        timer.cancel()
        isRunning = False
        switch()
        
    
def switch():
    if letsgoBtn["state"] == "normal":
        letsgoBtn["state"] = "disabled"
        entryMin["state"] = "disabled"
        stopBtn["state"] = "normal"
    else:
        letsgoBtn["state"] = "normal"
        entryMin["state"] = "normal"
        stopBtn["state"] = "disabled"

def finish():
    mb.showinfo(title='Time Over',message='Rest your eyes!')
    switch()
                
def onClose():
    if mb.askokcancel(title="Exit", message="Sure you want to exit?"):
        if(isRunning):
            timer.cancel()
        root.destroy()


if __name__ == '__main__':
    main()