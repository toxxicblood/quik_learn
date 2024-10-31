from tkinter import *
import customtkinter as ctk
from  PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*500')

def color_picker(choice):
    label.configure(text=choice,text_color=choice)

def color_picker2():
    label.configure(text=my_option.get(), text_color = my_option.get())

def yellow():
    my_option.set('yellow')
    label.cofigure(text= my_option.get(), text_color=my_option.get())
#set options for options menu
colors = ['red', 'green', 'blue']

#create options menu
my_option = ctk.CTkOptionMenu(root, values=colors,
                              #command = color_picker
                              )
my_option.pack(pady=20, padx=20)

label = ctk.CTkLabel(root,text='')
label.pack(pady=20, padx=20)

button = ctk.CTkButton(root,  text='coose',command = color_picker2)
button.pack(pady=10, padx=20)

yellow_button = ctk.CTkButton(root, text='yellow', command = yellow)
yellow_button.pack(pady=10, padx=20)


root.mainloop()