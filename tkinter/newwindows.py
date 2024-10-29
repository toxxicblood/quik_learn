from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

def new():
    #in new windows we cand to much customisation
    new_window = ctk.CTkToplevel(root)
    new_window.title('New Window')
    new_window.geometry('300*200')
    #new_window.resizeable(False, False)#width and height


    def close():
        new_window.destroy()
        new_window.update()
    #putthing things in the window
    #closing window
    new_button =ctk.CTkButton(new_window, text= 'close window', command =close)
    new_button.pack(pady=40)

button = ctk.CTkButton(root, text ='open new window', command = new)
button.pack(pady=20)



root.mainloop()