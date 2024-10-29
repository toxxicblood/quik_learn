from tkinter import *
import customtkinter as ctk
import random


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

    
family=['Times','times', 'sans-serif', 'arial','serif',
    'monospace', 'script', 'display',
    'handwriting','blackletter','modern']
specific= random.randint(1,10)
size = random.randint(1,50),
weight=['bold','normal']
slant = ['italic','roman']
underline=[True, False]
overstrike=[True, False]

my_font = ctk.CTkFont(
    family=f'{random.choice(family)}{specific}',
    size=random.randint (10,50),
    weight=random.choice(weight),
    slant=random.choice(slant),
    underline=random.choice(underline),
    overstrike= random.choice(overstrike),
)
    
def change():
    my_font.configure(
        family=f'{random.choice(family)}{specific}',
        size=random.randint (10,50),
        weight=random.choice(weight),
        slant=random.choice(slant),
        underline=random.choice(underline),
        overstrike= random.choice(overstrike),
    )               
#the way we have been changing font makes it fixed but there is a way where  we can change
#the font progreamatically
my_label = ctk.CTkLabel(root, text= "font_automix ABc", font=my_font)
my_label.pack(pady=20, padx=20)

my_button = ctk.CTkButton(root, text='Change font', command=change)
my_button.pack()


root.mainloop()