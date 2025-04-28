from tkinter import *
import tkinter as tk


import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import sqlite3
# import tfModel_test as tf_test
global fn
fn = ""
root = tk.Tk()
root.title("HomePage ")
root.geometry("1400x900")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
img = Image.open("C:/Users/Administrator/Desktop/Pysiotherapy pose detection/Images/111.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)

# #####For background Image
image2 = Image.open('C:/Users/Administrator/Desktop/Pysiotherapy pose detection/Images/i2.jpeg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


label_l1 = tk.Label(root, text="Physiotherapy Pose Detection Using Machine Learning",font=("Times New Roman", 18, 'bold'),
                    background="#647C90", fg="white", width=75, height=2)
label_l1.place(x=100, y=0)



from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])
    
    

def window():
    root.destroy()


d1=tk.Button(root,text="Login",command=Login,width=20,height=2,bd=0,background="#647C90",foreground="white",font=("times new roman",14,"bold"))
d1.place(x=1000,y=0)

d2=tk.Button(root,text="Register",command=Register,width=20,height=2,bd=0,background="#647C90",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1150,y=00)


d3=tk.Button(root,text="Exit",command=window,width=20,height=2,bd=0,background="#647C90",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1400,y=0)




root.mainloop()
