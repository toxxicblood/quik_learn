from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

def get_rad():
    if radio_var.get() == 'build to sell':
        my_label2.configure(text='okay serial enterprenour, up you grand slam offers')
    elif radio_var.get() == 'build to own':
        my_label2.configure(text='okay big fish, make sure inflow > outflow')
    elif radio_var.get() == "worker ant":
        my_label2.configure (text='okay worker ant, make sure you have a plan')
    else:
        my_label2.configure(text='make you fucking  mind up')

my_label = ctk.CTkLabel(root, text='whats your goal?', font =('Arial',18))
my_label.pack(pady=10)

my_label2 = ctk.CTkLabel(root, text='', font =('Arial',18))
my_label2.pack(pady=10)


radio_var = ctk.StringVar(value= 'other')
#to customise radio buttons you have to customise each of them.
#customisations are of the same schema. ill show with one example,  you can do the rest.
#create radiobutton 1
my_rad1 = ctk.CTkRadioButton(root, text='build bussinesses to sell', 
                             value='build to sell',
                             variable= radio_var,
                             #width=50
                             #height=50
                             #radiobutton_width=50
                             #radiodbutton_height=50
                             corner_radius=5,
                             border_width_unchecked=2,
                             border_width_checked=5,
                             border_color='red',
                             hover_color= 'yellow',
                             fg_color='green',
                             #hover=false
                             text_color=  'blue',
                             font = ('Arial',18),
                             #state= 'disabled',#or normal
                             text_color_disabled = 'charcoal'

                             )
my_rad1.pack(pady=10)
#create a second radio button
my_rad2 = ctk.CTkRadioButton(root, text='build bussinesses to own', 
                             value='build to own',
                             variable= radio_var,
                             
                             )
my_rad2.pack(pady=10)

#create a third radio button
my_rad3 = ctk.CTkRadioButton(root, text='work a 9-5', 
                             value='worker ant',
                             variable= radio_var,
                             
                             )
my_rad3.pack(pady=10)

my_button = ctk.CTkButton(root, text="confirm selection", command = get_rad)
my_button.pack(pady=10)

root.mainloop()