#GUIPRACTICEAGAIN

import tkinter as tk
from tkinter import *
from WoWDBConnector import get_weapons

Simulator = tk.Tk()


Simulator.title("Fury Simulator")
Simulator.geometry("900x300")

instructions = tk.Label(Simulator , text = "This is intended to be a ghetto simulation.\n"
"Most buffs are held constant.")
instructions.pack()

#Update the listbox
def update(weapon_query):
    #Clear the listbox
    weapons_list.delete(0 , END)
    #Add weapons to listbox
    for items in weapon_query:
        weapons_list.insert(END , items)

#update entry box with listbox click
def fillout(event):
    #delete what is in in entry box
    weapon_input.delete(0 , END)
    #adds the click even from the user
    weapon_input.insert(0 , weapons_list.get(ACTIVE))

#Create an entry box , field that the user inputs
weapon_label = tk.Label(Simulator , text = 'Enter weapon here: ')
weapon_label.pack()
weapon_input = tk.Entry(Simulator)


# weapon_input.bind('<Enter>' , enter_pressed)
weapon_input.pack()


#create listbox
weapons_list = Listbox(Simulator , width = 50 , height = 5)
weapons_list.pack()


#pulls list of weapons user can select
weapon_query = get_weapons()
update(weapon_query)


#checks entry against the imported listbox
def check_listbox(event):
    #get what is user_input
    user_input = weapon_input.get()
    if user_input == '':
        list_data = weapon_query
    else:
        list_data = []
        for item in weapon_query:
            if user_input.lower() in item.lower():
                list_data.append(item)

    #update listbox with selected item
    update(list_data)


#Listboxs = <<>> , single actions = <> , select from the listbox
weapons_list.bind("<<ListboxSelect>>" , fillout)

#Create binding on entry box to autofill
weapon_input.bind("<KeyRelease>" , check_listbox)

duration_label = tk.Label(Simulator , text = 'Number of iterations:')
duration_label.pack()
duration_label1 = Spinbox(Simulator , from_ = 60 , to_= 600)
duration_label1.pack()

button = tk.Button(Simulator , text = "Begin Simulation" )
button.pack()

##### Use pop out window for comparisons


Simulator.mainloop()