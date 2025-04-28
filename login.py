import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2

##############################################+=============================================================
root = tk.Tk()
root.configure(background="skyblue")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login Form")
img = Image.open("C:/Users/Administrator/Desktop/Pysiotherapy pose detection/Images/111.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)



username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('C:/Users/Administrator/Desktop/Pysiotherapy pose detection/Images/1.webp')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)




# img=ImageTk.PhotoImage(Image.open("l1.jpg"))

# img2=ImageTk.PhotoImage(Image.open("l2.jpg"))

# img3=ImageTk.PhotoImage(Image.open("l3.jpg"))


# logo_label=tk.Label()
# logo_label.place(x=700,y=10)

# x = 1

# # function to change to next image
# def move():
# 	global x
# 	if x == 4:
# 		x = 1
# 	if x == 1:
# 		logo_label.config(image=img, width=700, height=700)
# 	elif x == 2:
# 		logo_label.config(image=img2, width=700, height=700)
# 	elif x == 3:
# 		logo_label.config(image=img3, width=700, height=700)
# 	x = x+1
# 	root.after(2000, move)

# # calling the function
# move()


def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()



def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(Fullname TEXT, username TEXT, Email TEXT, password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            
            from subprocess import call
            call(["python","Home.py"])
            root.destroy()
            # ===========================================
            

          
            # cap = cv2.VideoCapture(0)
            
            # while(True): 
            #     # Capture frame-by-frame
                
            #     ret, frame = cap.read()
                
            #     # Display the resulting frame
                
            #     cv2.imshow('Preview',frame)
                
            #     #Waits for a user input to quit the application
                
            #     if cv2.waitKey(1) & 0xFF == ord('q'):
                
            #         break

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
          
          
           


# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


# bg1_icon=ImageTk.PhotoImage(file="D:\\module\30 % code\\30 % code\\b2.png")

# bg_icon=ImageTk.PhotoImage(file="L.jpg")
# user_icon=ImageTk.PhotoImage(file="u1.png")
# pass_icon=ImageTk.PhotoImage(file="p1.jpg")
        
# bg_lbl=tk.Label(root,image=bg1_icon, width=600,height=600)
# bg_lbl.place(x=50,y=50)
        
# title=tk.Label(root, text="Login Here", font=("Algerian", 30, "bold","italic"),bd=5,bg="skyblue",fg="black")
# title.place(x=900,y=115,width=250)
        
Login_frame=tk.Frame(root,bg="#A5ABA0")
Login_frame.place(x=505,y=250)
        
logolbl=tk.Label(Login_frame,text="Login Here",font=("Algerian", 30, "bold","italic"),bd=5,bg="#A5ABA0",fg="black").grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Username", compound=LEFT,font=("Times new roman", 20, "bold"),bg="#A5ABA0").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=0,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password", compound=LEFT,font=("Times new roman", 20, "bold"),bg="#A5ABA0").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=0,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="#A5ABA0",fg="black", bd=1)
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="#A5ABA0",fg="black", bd=1)
btn_reg.grid(row=3,column=0,pady=10)
        
        
    

root.mainloop()