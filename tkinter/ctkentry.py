#here we check entry boxes
from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

def submit():
    my_label.configure(text=f'fuck off {my_entry.get()}')
    my_entry.configure(state= "disabled")

def clear():
    my_entry.delete(0, END)#end is supplied by tkinter
    my_entry.configure(state= "normal")

my_label = ctk.CTkLabel(root, text='', font=("Helvetica", 20))
my_label.pack(pady = 40)

my_entry = ctk.CTkEntry(root,
                         placeholder_text= "Name",
                         height=50,
                         width=200,
                         font= ("Helvetica", 18),
                         corner_radius=50,
                         text_color="magenta",
                         placeholder_text_color= "cyan",
                         fg_color=("blue","maroon"),#outer color, inner color
                         
                         )
my_entry.pack(pady=20)

my_button = ctk.CTkButton(root, text='submit', command= submit)
my_button.pack(pady=10)

clear_button = ctk.CTkButton(root, text="clear", command=clear)
clear_button.pack(pady=10)




root.mainloop()