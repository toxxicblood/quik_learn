from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

#input function
def input():
    #this is the popup.
    #like everything else you can customise it however you want
    dialog= ctk.CTkInputDialog(title="Input", text="Enter your name")
    thing = dialog.get_input()
    if thing:
        label.configure (text=F"Hello{thing}")

    else:
        label.configure (text=F"fuckin type summ")
#create button
button =  ctk.CTkButton(root, text='Click me', command=input)
button.pack(pady=20)

#create label
label = ctk.CTkLabel(root, text='')
label.pack(pady=20)

root.mainloop()