from tkinter import *
import customtkinter as ctk
#from  PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("themes/red.json")
#ctk.deactivate_automatic_dpi_awareness()
ctk.set_widget_scaling(0.5)  # widget dimensions and text size
ctk.set_window_scaling(1.5)  # window geometry dimensions
#for the above assume 1.0 is 100%
root = ctk.CTk()

root.title('ctk')
root.geometry('600*500')

def change_colors(choice):
    ctk.set_default_color_theme(choice)
mode = 'dark'
def change():
    global mode
    if mode == 'dark':
        ctk.set_appearance_mode('light')
        mode = 'light'
        #clear text box
        my_text.delete(0.0, END)
        my_text.insert(0.0, 'Light Mode')
    else:
        ctk.set_appearance_mode('dark')
        mode = 'dark'
        #clear text box
        my_text.delete(0.0, END)
        my_text.insert(0.0, 'Dark Mode')


my_text = ctk.CTkTextbox(root, width=600, height=300)
my_text.pack(pady=20, padx=20)

my_button = ctk.CTkButton(root, text='change theme', command = change )
my_button.pack(pady=20, padx=20)

colors = ['blue', 'dark-blue', 'green']
my_option = ctk.CTkOptionMenu(root, values = colors , command= change_colors)
my_option.pack(pady=20, padx=20)

root.mainloop()