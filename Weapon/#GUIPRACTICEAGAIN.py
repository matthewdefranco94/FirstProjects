#GUIPRACTICEAGAIN

import tkinter as tk
from tkinter import *


Simulator = tk.Tk()


Simulator.title("Fury Simulator")
Simulator.geometry("900x300")

instructions = tk.Label(Simulator , text = "This is intended to be a ghetto simulation.\n"
"Most buffs are held constant.")
instructions.place(relx = 0.5, rely = .1)

#Create an entry box
weapon_label = tk.Label(Simulator , text = 'Enter weapon here: ')
weapon_label.place(relx = .4 , rely = .3)
weapon_input = tk.Entry(Simulator)
weapon_input.place(relx = .75 , rely = .3 )

#create listbox
weapons_list = Listbox(Simulator , width = 50 , height = 20)
weapons_list.place(relx = .75 , rely = .5)


duration_label = tk.Label(Simulator , text = 'Number of iterations:')
duration_label.place(relx = .4 , rely = .4)
duration_label1 = Spinbox(Simulator , from_ = 60 , to_= 600)
duration_label1.place(relx = .75 , rely = .4)

button = tk.Button(Simulator , text = "Enter" )
button.place(relx = .9 , rely = .3)

Simulator.mainloop()