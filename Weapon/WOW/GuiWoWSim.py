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


def user_input(label , max_box):
    input_label = tk.Label(Simulator , text = label )
    input_label.pack()
    spinbox_labeler = tk.Spinbox(Simulator , from_ = 0 , to_ = max_box)
    spinbox_labeler.pack()
    return spinbox_labeler



user_hit_chance = user_input('What is your total hit chance' , 60)

user_crit_chance = user_input("What is your critical chance?" , 60)

user_weapskill = user_input('What is your added weapon skill?' , 60)

user_fight_duration = user_input('How long is your fight in seconds? (no longer than 6 minutes)' , 600 )

user_iterations = user_input('Number of iterations:' , 200)





#Create binding on entry box to autofill
weapon_input.bind("<KeyRelease>" , check_listbox)

#Listboxs = <<>> , single actions = <> , select from the listbox
weapons_list.bind("<<ListboxSelect>>" , fillout)


button = tk.Button(Simulator , text = "Begin Simulation" , command = lambda: button_action(weapon_input.get()))
button.pack()



def button_action(weapon_input):
    weapon_stats = get_weapon_stats(weapon_input)
    result = do_simulation( int(weapon_stats['dmg_min1']),
                            int(weapon_stats['dmg_max1']),
                            int(weapon_stats['delay'])/1000,
                            int(user_hit_chance.get()), int(user_crit_chance.get()),
                            int(user_weapskill.get()), int(user_iterations.get()))
    #saying result is equal to what 'do_simulation' gives back

    print(result.total_damage)
        

    print(f"Your total damage across {result.number_of_attacks} attacks is {round(sum(result.total_damage))}")
    #Damage per second accounting for other variables
    DPS = float(sum(result.total_damage)) / int(result.fight_duration)
    DPS = round(result.average_DPS)
    print("You deal an average of " + str(result.average_DPS) + " DPS over a " + str(round(result.fight_duration / 60)) + " minute long fight.")
    print("Your static weapon DPS is " + str(result.weapon_DPS) + ".")
    
    #number of missed attacks
    miss_count = result.total_damage.count(0)
    print("Your number of missed attacks is " + str(miss_count) + ".")
    
    

##### Use pop out window for comparisons?maybe


Simulator.mainloop()