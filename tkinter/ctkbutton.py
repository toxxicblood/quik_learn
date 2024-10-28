import tkinter as tk
import customtkinter as ctk

#set the theme color options 
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")#three colors to choose from blue, dark-blue, green

#root = Tk()
root = ctk.CTk()

root.title("customtkinter")
root.geometry("600*350")

def hello():
    my_label.configure(text='fuck off')
    my_label.configure(text=my_button.cget("text"))


my_button = ctk.CTkButton(root, 
                          text="wagwan rammah", 
                          command= hello,
                          height=100,
                          width=200,
                          font=("Helvetica", 24),
                          text_color='blue',
                          fg_color='black',
                          hover_color= 'green',
                          corner_radius= 50,
                          bg_color= 'yellow',
                          border_width=10,
                          border_color='pink',
                          state='disabled'#or normal
                          
                          )
my_button.pack(pady=80)

my_label= ctk.CTkLabel(root, text="")
my_label.pack(pady=20)
root.mainloop()