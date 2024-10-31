from tkinter import *
import customtkinter as ctk
#from  PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def  __init__(self):
        super().__init__()

    #self = ctk.CTk()

        self.title('ctk')
        self.geometry('600*500')

     

        self.my_text = ctk.CTkTextbox(self, width=600, height =300)
        self.my_text.pack(pady=20, padx=20)

        self.my_button = ctk.CTkButton(self, text='clear', command = self.clear)
        self.my_button.pack(pady=20)

    def clear(self):
        self.my_text.delete(0.0, END)

#create main loop
app = App()
app.mainloop()