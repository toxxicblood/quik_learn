from tkinter import *
import customtkinter as ctk
#from  PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('1000*700')

global my_y
my_y =700/2 + 350

def up():
    global my_y
    my_y -=1
    if my_y >=200:
        my_text.place(x=1000/2, y=my_y, anchor='center')
        upbutton.configure(text=my_y)
        root.after(2, up)
        

def down():
    global my_y
    my_y +=1
    if my_y <=700:
        my_text.place(x=1000/2, y=my_y, anchor='center')
        downbutton.configure(text=my_y)
        root.after(2, down)


my_frame =ctk.CTkFrame(root)
my_frame.pack(pady=20)

upbutton = ctk.CTkButton(my_frame, text = 'up', command = up)
upbutton.grid(row=0, column=0, padx=10)

downbutton= ctk.CTkButton(my_frame, text= 'down', command =down)
downbutton.grid(row=0, column=1, padx=10)
 
#text box
my_text = ctk.CTkTextbox(root, width=400, height=200)
#place allows us to very specific place coordinates
my_text.place(x=1000/2, y=my_y, anchor='center')

root.mainloop()