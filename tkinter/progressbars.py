from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

def clicker():
    my_progressbar.step()
    my_label.configure(text=(int(my_progressbar.get()*100)))

def start():
    my_progressbar.start()

def stop():
    my_progressbar.stop()

my_progressbar= ctk.CTkProgressBar(root, 
                                   width=70,
                                   height=22,
                                   orientation='horizontal',
                                   mode='indeterminate',
                                   determinate_speed=1,
                                   indeterminate_speed=0.5,
                                   corner_radius=10,
                                   border_width=10,
                                   #all customisations are virtually the same
                                   fg_color='#00ff00',
                                   #fg_color_activated='#00ffff',
                                   progress_color='orange'


                                   )
my_progressbar.pack(pady=40)

#set default starting point
my_progressbar.set(0)

my_button = ctk.CTkButton(root ,text='click me', command =clicker)
my_button.pack(pady=10)

start_button= ctk.CTkButton(root, text='start', command = start)
start_button.pack(pady=10)

stop_button= ctk.CTkButton(root, text='stop', command = stop)
stop_button.pack(pady=10)


my_label = ctk.CTkLabel(root, text='', font =('Arial',18))
my_label.pack(pady=10)



root.mainloop()