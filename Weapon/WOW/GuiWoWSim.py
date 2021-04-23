#GUIPRACTICEAGAIN

import tkinter as tk
from tkinter import *
from WoWDBConnector import *
from WeapSimPractice import do_simulation



Simulator = tk.Tk()


Simulator.title("Fury Simulator")
Simulator.geometry("900x300")

instructions = tk.Label(Simulator , text = "This is intended to be a ghetto simulation.\n"
"Most buffs are held constant.")
instructions.pack()

#Update the listbox
def update(weapon_query_1):
    #Clear the listbox
    weapons_list.delete(0 , END)
    #Add weapons to listbox
    # print(type(weapon_query_1))
    for items in weapon_query_1:
        # print(type(items))
        weapons_list.insert(0 , items)
        

#update entry box with listbox click
def fillout(event):
    #delete what is in in entry box
    weapon_input.delete(0 , END)
    #adds the click event from the user
    weapon_input.insert(0 , weapons_list.get(ACTIVE))

#Create an entry box , field that the user inputs
weapon_label = tk.Label(Simulator , text = 'Enter weapon here: ')
weapon_label.pack()
weapon_input = tk.Entry(Simulator)   ####user's weapon input


# weapon_input.bind('<Enter>' , enter_pressed)
weapon_input.pack()


#create listbox
weapons_list = Listbox(Simulator , width = 50 , height = 5)
weapons_list.pack()


#pulls list of weapons user can select
weapon_query = get_weapons()
update(weapon_query)                  ####original location

#checks entry against the imported listbox  
def check_listbox(event):
    #get what is user_input
    user_input = weapon_input.get()
    list_data = []
    if user_input == '':
        for weapon in weapon_query:
            list_data.append(weapon)
    else:
        for weapon in weapon_query:
            if user_input.lower() in weapon.lower():
                list_data.append(weapon)

    #update listbox with selected item
    update(list_data)


#Create binding on entry box to autofill
weapon_input.bind("<KeyRelease>" , check_listbox)

#Listboxs = <<>> , single actions = <> , select from the listbox
weapons_list.bind("<<ListboxSelect>>" , fillout)

duration_label = tk.Label(Simulator , text = 'Number of iterations:')
duration_label.pack()
duration_label1 = Spinbox(Simulator , from_ = 60 , to_= 600)
duration_label1.pack()


button = tk.Button(Simulator , text = "Begin Simulation" , command = lambda: button_action(weapon_input.get()))
button.pack()



def button_action(weapon_input):
    weapon_stats = get_weapon_stats(weapon_input)
    do_simulation(weapon_stats['dmg_min1'],weapon_stats['dmg_max1'],weapon_stats['delay']/1000,5,40,5,120)
    
    
    

##### Use pop out window for comparisons?maybe


Simulator.mainloop()