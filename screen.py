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
label_text.place(x=400, y=10)


#Button

button_start = Button(screen, width=6, height=1, text="START", font=("Arial 15 bold") ,relief="solid", fg="#ffffff", bg="#BD0000")
button_start.place(x=800, y=67)


textarea = Entry(screen, width=22, font=("Aria 15 bold"))
textarea.place(x=470, y=70)


screen.mainloop()