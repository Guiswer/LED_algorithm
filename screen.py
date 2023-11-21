from tkinter import *

#colors

#Background color
background_color = "#001622"


#Screen

screen = Tk()
screen.title("LEDinPYTHON")
screen.geometry('1280x720')
screen.config(bg=background_color)


#Icon

screen.iconphoto(False, PhotoImage(file="img/8segmentos.png"))
screen.resizable(width=False, height=False)


#Label 'Type a word:'

label_text = Label(screen, width=20, height=2, font=("Arial 20 bold"), fg="#ffffff", bg=background_color, text='Type a word:')
label_text.grid(row=10, column=0, pady=30, padx=490)


screen.mainloop()