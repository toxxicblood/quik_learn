from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

def game():
    if check_var.get() == "on":
        my_label.configure(text= "app started")
    else:
        my_label.configure(text= "app stopped")

    text_var.set("app launch ready for confirmation")

def clear_me():
    my_check.deselect()
    text_var.set('app launch cancelled')

#checkbox state
check_var= ctk.StringVar(value="off")# or IntVar(value=2)
#checkbox text
text_var = ctk.StringVar(value='start an app')
my_check = ctk.CTkCheckBox(root, 
                           text= 'start an app',
                           variable=check_var,
                           onvalue='on',
                           offvalue= 'off',
                           checkbox_width = 30,
                           checkbox_height = 30,
                           font=  ('Arial', 10),
                           corner_radius=50,
                           fg_color="red",
                           hover_color="magenta",
                           text_color= "cyan",
                           hover = False,
                           textvariable=text_var,
                           )
my_check.pack(pady=40)

my_button = ctk.CTkButton(root, text="confirm", command= game)
my_button.pack(pady=20)

clear_button = ctk.CTkButton(root, text= 'clear' , command= clear_me)
clear_button.pack(pady=20)

toggle_button = ctk.CTkButton(root, text= 'toggle' , command= my_check.toggle)
toggle_button.pack(pady=20)

select_button= ctk.CTkButton(root, text= 'select' , command= my_check.select)
select_button.pack(pady=20)

my_label = ctk.CTkLabel(root, text='')
my_label.pack(pady=20)

root.mainloop()