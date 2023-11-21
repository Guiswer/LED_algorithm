from tkinter import *
import time



#colors

#Background color
background_color = "#001622"


#Functions of letters

def ledA():
    led_a.config(bg="#ffffff")
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg=background_color)
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledB():
    led_a.config(bg=background_color)  
    led_b.config(bg=background_color)
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledC():
    led_a.config(bg="#ffffff")
    led_b.config(bg=background_color)
    led_c.config(bg=background_color)
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg=background_color)


def ledD():
    led_a.config(bg=background_color)  
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg=background_color)
    led_g.config(bg="#ffffff")


def ledE():
    led_a.config(bg="#ffffff") 
    led_b.config(bg="#ffffff")
    led_c.config(bg=background_color)
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledF():
    led_a.config(bg="#ffffff")
    led_b.config(bg=background_color)
    led_c.config(bg=background_color) 
    led_d.config(bg=background_color)
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledG():
    led_a.config(bg="#ffffff")
    led_b.config(bg=background_color)
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledH():
    led_a.config(bg=background_color) 
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg=background_color)
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledI():
    led_a.config(bg=background_color) 
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg=background_color)
    led_e.config(bg=background_color)
    led_f.config(bg=background_color)
    led_g.config(bg=background_color)


def ledJ():
    led_a.config(bg=background_color) 
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg=background_color)
    led_g.config(bg=background_color)


def ledL():
    led_a.config(bg=background_color) 
    led_b.config(bg=background_color)
    led_c.config(bg=background_color)
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg=background_color)


def ledO():
    led_a.config(bg="#ffffff") 
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg=background_color)


def ledP():
    led_a.config(bg="#ffffff") 
    led_b.config(bg="#ffffff")
    led_c.config(bg=background_color)
    led_d.config(bg=background_color)
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledQ():
    led_a.config(bg="#ffffff")
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg=background_color)
    led_e.config(bg=background_color)
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledR():
    led_a.config(bg="#ffffff")
    led_b.config(bg=background_color)
    led_c.config(bg=background_color)
    led_d.config(bg=background_color)
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg=background_color)    


def ledS():
    led_a.config(bg="#ffffff") 
    led_b.config(bg=background_color)
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg=background_color)
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")


def ledU():
    led_a.config(bg=background_color) 
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg="#ffffff")
    led_g.config(bg=background_color)


def ledY():
    led_a.config(bg=background_color)  
    led_b.config(bg="#ffffff")
    led_c.config(bg="#ffffff")
    led_d.config(bg=background_color)
    led_e.config(bg=background_color)
    led_f.config(bg="#ffffff")
    led_g.config(bg="#ffffff")

def ledZ():
    led_a.config(bg="#ffffff")
    led_b.config(bg="#ffffff")
    led_c.config(bg=background_color)
    led_d.config(bg="#ffffff")
    led_e.config(bg="#ffffff")
    led_f.config(bg=background_color)
    led_g.config(bg="#ffffff")


def exec(word_type):
    x = 0 

    if "k" in word_type or "m" in word_type or "n" in word_type or "t" in word_type or "v" in word_type or "w" in word_type or "x" in word_type:
        print("The letters: (k, m, n, t, v, w, x) are not allowed.")

    if word_type == "":
        print("Please, type a word.")

    else:
        while x < len(word_type):

            if word_type[x].lower() == "a":
                ledA()

            elif word_type[x].lower() == "b":
                ledB()

            elif word_type[x].lower() == "c":
                ledC()

            elif word_type[x].lower() == "d":
                ledD()

            elif word_type[x].lower() == "e":
                ledE()

            elif word_type[x].lower() == "f":
                ledF()

            elif word_type[x].lower() == "g":
                ledG()
                
            elif word_type[x].lower() == "h":
                ledH()

            elif word_type[x].lower() == "i":
                ledI()
                
            elif word_type[x].lower() == "j":
                ledJ()

            elif word_type[x].lower() == "l":
                ledL()

            elif word_type[x].lower() == "o":
                ledO()

            elif word_type[x].lower() == "p":
                ledP()

            elif word_type[x].lower() == "q":
                ledQ()

            elif word_type[x].lower() == "r":
                ledR()

            elif word_type[x].lower() == "s":
                ledS()

            elif word_type[x].lower() == "u":
                ledU()
                
            elif word_type[x].lower() == "y":
                ledY()
                
            elif word_type[x].lower() == "z":
                ledZ()

            x += 1 

   
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

label_text = Label(screen, width=20, height=2, font=("Arial 20 bold"), fg="#ffffff", bg=background_color, bd=0,text='Type a word:')
label_text.place(x=400, y=10)


#Button

button_start = Button(screen, command=lambda: exec(textarea.get()), width=6, height=1, text="START", font=("Arial 15 bold") ,relief="solid", fg="#ffffff", bg="#BD0000", highlightthickness=3, highlightbackground="#E33535", bd=0)
button_start.place(x=800, y=67)


#Entry

textarea = Entry(screen, width=22, font=("Aria 15 bold"), bg="#18597D", bd=0, fg="#ffffff", highlightthickness=0)
textarea.place(x=470, y=70)


#LEDs

led_a = Frame(screen, width=150, height=30, bg="#00324E")
led_a.place(x=557, y=170)


led_b = Frame(screen, width=30, height=150, bg="#00324E")
led_b.place(x=707, y=200)


led_c = Frame(screen, width=30, height=150, bg="#00324E")
led_c.place(x=707, y=380)


led_d = Frame(screen, width=150, height=30, bg="#00324E")
led_d.place(x=557, y=530)


led_e = Frame(screen, width=30, height=150, bg="#00324E")
led_e.place(x=527, y=380)


led_f = Frame(screen, width=30, height=150, bg="#00324E")
led_f.place(x=527, y=200)


led_g = Frame(screen, width=150, height=30, bg="#00324E")
led_g.place(x=557, y=350)


screen.mainloop()