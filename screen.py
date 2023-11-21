from tkinter import *


#function_get

def function_get():
	word_type = textarea.get()


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


#By Guiswer

label_by = Label(screen, bg="#001622", fg="cyan", width=10, text="By: Guiswer", font=("Aria 10 bold"))
label_by.place(x=10, y=1)

#Label 'Type a word:'

label_text = Label(screen, width=20, height=2, font=("Arial 20 bold"), fg="#ffffff", bg=background_color, text='Type a word:')
label_text.place(x=400, y=10)


#Button

button_start = Button(screen, command=function_get, width=6, height=1, text="START", font=("Arial 15 bold") ,relief="solid", fg="#ffffff", bg="#BD0000")
button_start.place(x=800, y=67)


#Entry

textarea = Entry(screen, width=22, font=("Aria 15 bold"), bg="#18597D", fg="#ffffff")
textarea.place(x=470, y=70)


#LEDs

led_a = Frame(screen, width=150, height=30, bg="#ffffff")
led_a.place(x=557, y=170)


led_b = Frame(screen, width=30, height=150, bg="#ffffff")
led_b.place(x=707, y=200)


led_c = Frame(screen, width=30, height=150, bg="#ffffff")
led_c.place(x=707, y=380)


led_d = Frame(screen, width=150, height=30, bg="#ffffff")
led_d.place(x=557, y=530)


led_e = Frame(screen, width=30, height=150, bg="#ffffff")
led_e.place(x=527, y=380)


led_f = Frame(screen, width=30, height=150, bg="#ffffff")
led_f.place(x=527, y=200)


led_g = Frame(screen, width=150, height=30, bg="#ffffff")
led_g.place(x=557, y=350)



screen.mainloop()