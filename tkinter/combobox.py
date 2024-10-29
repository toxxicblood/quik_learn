from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')


def color_picker(choice):
    output_label.configure(text=choice, text_color= choice)

def color_picker2():
    output_label.configure(text= my_combo.get(), text_color=my_combo.get())

def color_picker_green():
    #set combo box option
    my_combo.set('green')
    output_label.configure(text="green", text_color="green")


my_label = ctk.CTkLabel(root, text='pick a color', font= ('Arial',40))
my_label.pack(pady=20)


#set options for combobox
color = ['red', 'cyan', 'blue', 'maroon', 'mustard', 'khaki']
#create combobox
my_combo = ctk.CTkComboBox(root, 
                           values= color,
                           #height=30,
                           #width=40,
                           font =('Arial', 12),
                           dropdown_font =('Arial', 12),
                           corner_radius=35,
                           border_width=10,
                           border_color='yellow',
                           button_color='yellow',
                           button_hover_color='cyan',
                           dropdown_hover_color='blue',
                           dropdown_fg_color='yellow',
                           dropdown_text_color='orange',
                           text_color='silver',
                           hover=True,
                           justify='left',
                           state='disabled' #or normal,

                           )
my_combo.pack(pady=10)

#create a button
my_button = ctk.CTkButton(root, text='Pick a color', command=color_picker2)
my_button.pack(pady=10)

#custom/default button
green_button= ctk.CTkButton(root, text='pick green', command=color_picker_green)
green_button.pack(pady=10)

#output labe
output_label = ctk.CTkLabel(root, text='', font=('Arial', 20))
output_label.pack(pady=10)


root.mainloop()