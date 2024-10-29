from tkinter import *
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()

root.title('ctk')
root.geometry('600*300')

#create a scrollable frame
#customisation is virtually the same as everything else
my_frame = ctk.CTkScrollableFrame(root,
                                #orientation='horisontal', or 'vertical'
                                #width=3
                                #height =4
                                label_text= 'wagwan ramsey',
                                label_fg_color = 'pink',
                                label_text_color= 'black',
                                label_font = ('Times New Roman 17',8),
                                label_anchor = 'center' ,#available directions are  n, s, e, w, ne, se, sw, nw, center
                                border_width = 1,
                                border_color= 'pink',
                                fg_color = 'blue',
                                scrollbar_fg_color= 'pink',
                                scrollbar_button_color = 'black'
                                )
my_frame.pack(pady=40)


#for loop for buttons
for x in range(20):
    ctk.CTkButton(my_frame, text=f'Button{x}').pack(pady=7)



root.mainloop()