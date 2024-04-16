from tkinter import * # arxh
import random

win = Tk()

win.title("parathiri")
win.geometry('460x350')
win.configure(background="#231E36")


tries = 0
easy = 0
normal = 0
hard = 0
up = PhotoImage(file = "uparrow.png")
down = PhotoImage(file = "downarrow.png")
dice = PhotoImage(file = "dice.png")
check = PhotoImage(file = "correct.png")
questionmarks = PhotoImage(file = "questionmarks.png")

def exit():
    win.destroy()

def randomize():
    piclbl.configure(image = dice)
    numberentry.configure(state = 'normal')
    randombtn.configure(state = 'disabled')
    global randomnumber
    if var.get() == 'easy':
        global easy
        randomnumber = random.randint(0,50)
        print(randomnumber)
        easy = 1
    elif var.get() == 'normal':
        global normal
        randomnumber = random.randint(0,100)
        print(randomnumber)
        normal = 1
    elif var.get() == 'hard':
        global hard
        randomnumber = random.randint(0,200)
        print(randomnumber)
        hard = 1


def game(*args):
    global tries
    # 1. check entry number me to random number tou pc
    # 1c. iso ? deiske check
    if easy == 1:
        if int(numberentry.get()) > 50 or int(numberentry.get()) < 0:
            numberentry.delete(0, END)
            piclbl.configure(image=questionmarks)
            vrisidilbl.configure(foreground='yellow')
        else:
            if int(numberentry.get()) == randomnumber:
                numberentry.delete(0, END)
                numberentry.configure(state = 'disabled')
                piclbl.configure(image = check)
                vrisidilbl.configure(foreground="#261E36")
        # 1a. megalytero ? deiske katw velaki
            elif int(numberentry.get()) > randomnumber:
                numberentry.delete(0, END)
                piclbl.configure(image = down)
                tries += 1
                trieslbl.configure(text = "Tries: " + str(tries))
                vrisidilbl.configure(foreground="#261E36")
        # 1b. mikrotero? deiske panw velaki
            elif int(numberentry.get()) < randomnumber:
                numberentry.delete(0, END)
                piclbl.configure(image=up)
                tries += 1
                trieslbl.configure(text="Tries: " + str(tries))
                vrisidilbl.configure(foreground="#261E36")

    if normal == 1:
        if int(numberentry.get()) > 100 or int(numberentry.get()) < 0:
            print(numberentry.get() > str(100))
            numberentry.delete(0, END)
            piclbl.configure(image=questionmarks)
            vrisidilbl.configure(foreground='yellow')
        else:
            if int(numberentry.get()) == randomnumber:
                numberentry.delete(0, END)
                numberentry.configure(state='disabled')
                piclbl.configure(image=check)
                vrisidilbl.configure(foreground="#261E36")
            # 1a. megalytero ? deiske katw velaki
            elif int(numberentry.get()) > randomnumber:
                numberentry.delete(0, END)
                piclbl.configure(image=down)
                tries += 1
                trieslbl.configure(text="Tries: " + str(tries))
                vrisidilbl.configure(foreground="#261E36")
            # 1b. mikrotero? deiske panw velaki
            elif int(numberentry.get()) < randomnumber:
                numberentry.delete(0, END)
                piclbl.configure(image=up)
                tries += 1
                trieslbl.configure(text="Tries: " + str(tries))
                vrisidilbl.configure(foreground="#261E36")

    if hard == 1:
        if int(numberentry.get()) > 200 or int(numberentry.get()) < 0:
            numberentry.delete(0, END)
            piclbl.configure(image=questionmarks)
            vrisidilbl.configure(foreground='yellow')
        else:
            if int(numberentry.get()) == randomnumber:
                numberentry.delete(0, END)
                numberentry.configure(state = 'disabled')
                piclbl.configure(image = check)
                vrisidilbl.configure(foreground="#261E36")
        # 1a. megalytero ? deiske katw velaki
            elif int(numberentry.get()) > randomnumber:
                numberentry.delete(0, END)
                piclbl.configure(image = down)
                tries += 1
                trieslbl.configure(text = "Tries: " + str(tries))
                vrisidilbl.configure(foreground="#261E36")
        # 1b. mikrotero? deiske panw velaki
            elif int(numberentry.get()) < randomnumber:
                numberentry.delete(0, END)
                piclbl.configure(image=up)
                tries += 1
                trieslbl.configure(text="Tries: " + str(tries))
                vrisidilbl.configure(foreground="#261E36")

    if tries >= 0 and tries <= 5:
        trieslbl.configure(foreground="green")
    elif tries >= 6 and tries <= 10:
        trieslbl.configure(foreground="yellow")
    elif tries >= 10:
        trieslbl.configure(foreground="red")

piclbl = Label(win, image = dice, width = 150, height = 120)
piclbl.grid(row=5, column=0, rowspan=2)

titlelbl = Label(win , text="Guess the Number", background="#261E36", foreground="#16C1D4", font=('Helvetica', 20, 'bold'), justify=CENTER, borderwidth=10, relief="groove")
titlelbl.grid(row=0, column=0, columnspan=3)

var = StringVar()
var.set('normal')

easy = Radiobutton(win, text = "Easy(0-50)", variable=var, value = "easy", font = ('Arial', 14), background="#261E36", foreground="#16C1D4", borderwidth=10, relief="groove", selectcolor="#000000")
easy.grid(row=1, column=0)

normal = Radiobutton(win, text = "Normal(0-100)", variable=var, value = "normal", font = ('Arial', 14), background="#261E36", foreground="#16C1D4", borderwidth=10, relief="groove", selectcolor="#000000")
normal.grid(row=1, column=1)

hard = Radiobutton(win, text = "Hard(0-200)", variable=var, value = "hard", font = ('Arial', 14), background="#261E36", foreground="#16C1D4", borderwidth=10, relief="groove", selectcolor="#000000")
hard.grid(row=1, column=2)

gameinfolbl = Label(win, text="In this game you will try to find a secret number"
"\n It will randomly be chosen every round"
"\n Try to guess it with the least possible tries", font = ('Arial', 12), background="#261E36", foreground="#16C1D4")
gameinfolbl.grid(row=2, columnspan=3)

numberentry = Entry(win, width = 12, state = 'disabled')
numberentry.grid(row=5, column=1)

exitbtn = Button(win, text = "Exit", font = ('Arial', 14), width = 10, height = 2, command = exit)
exitbtn.grid(row=5, column=2)

randombtn = Button(win, text = "Randomize", font = ('Arial', 14), width = 10, height = 2, command = randomize)
randombtn.grid(row=6, column=2)

trieslbl = Label(win, text = "Tries: " + str(tries), font = ('Arial', 12), background="#261E36", foreground="yellow")
trieslbl.grid(row=6, column=1)

vrisidilbl = Label(win, text = "Are you dumb??", font = ('Arial', 12), background="#261E36", foreground="#261E36")
vrisidilbl.grid(row=7, column=1)


win.bind('<Return>', game)

win.mainloop() # telos

#auto-py-to-exe
