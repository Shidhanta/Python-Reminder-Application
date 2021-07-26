import time
from notification import *
import PIL
from PIL import Image,ImageTk 
from plyer import notification 
import tkinter as tk
HEIGHT= 500
WIDTH= 600


def notification_func():
    print("Create notification")
    t = title.get()
    m = message.get("1.0",tk.constants.END)
    print(t)
    print(m)
    notification_declaration(t,m)
   


if __name__ == '__main__' :

    root = tk.Tk()    
    

    img_file = Image.open('background.jpg')
    bg = ImageTk.PhotoImage(img_file)
    background_label= tk.Label(root,image =bg)
    background_label.place(relwidth=1,relheight=1)

    canvas = tk.Canvas(root, height=HEIGHT,width=WIDTH)
    canvas.pack()
    
    frame = tk.Frame(root, bg="#8187db",bd=5)
    frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

    title = tk.Entry(frame,font=40)
    title.place(relwidth=0.65,relheight=1)

    button = tk.Button(frame, text="Submit" , font=40, command=notification_func)
    button.place(relx=0.7,relheight=1,relwidth=0.3)

    lower_frame = tk.Frame(root, bg="#8187db", bd=10)
    lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

    message = tk.Text(lower_frame, font=40)
    message.place(relwidth=1,relheight=1)

    root.mainloop()

 

