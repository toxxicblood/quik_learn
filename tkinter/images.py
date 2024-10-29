from tkinter import *
import customtkinter as ctk
from  PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*500')


image = ctk.CTkImage(
    #light_image = Image.open('images/911 banner.jpeg'),#or C:/whatever/
    dark_image = Image.open('images/porsche banner.jpeg'),
    size=(740, 450),#width by height
)
my_label = ctk.CTkLabel(root, text='', image= image)
my_label.pack()


root.mainloop()