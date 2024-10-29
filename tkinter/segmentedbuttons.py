from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

#create clicker function
def clicker(value):
    label.configure(text= f"is that a!!!! FUCKIN {my_seg_button.get()}")

#our button values
my_values = ['eliminator', 'bernelli', 'zx6r', 'r6', 'dirtbike','porsche']
#customisations are similar to all other widgets
my_seg_button = ctk.CTkSegmentedButton(root, values= my_values,
                                      command = clicker,
                                      dynamic_resizing= True, #or false
                                      
                                        
                                      )
my_seg_button.pack(pady=20)

# to set a default selection
# the selection must be on the list 
#NOTE: a default value does not trigger  the command 
#my_seg_button.set('porsche')


#label
label = ctk.CTkLabel(root, text="", font=("Arial",18))
label.pack(pady=20)

root.mainloop()