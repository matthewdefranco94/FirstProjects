#GUIPRACTICEAGAIN

import tkinter as tk
from tkinter import *
from WoWDBConnector import *
from WeapSimPractice import do_simulation



class WoWSimGui:
    def __init__(self , width = 900 , height = 400):

        self.Simulator = tk.Tk()


        self.Simulator.title("Fury Simulator")
        self.Simulator.geometry(str(width)+'x'+str(height)) #WxH

        self.instructions = tk.Label(self.Simulator , text = "This is intended to be a simulation.\n"
        "Most buffs are held constant.")
        self.instructions.pack()


        #Create an entry box , field that the user inputs
        self.weapon_label = tk.Label(self.Simulator , text = 'Enter weapon here: ')
        self.weapon_label.pack()
        self.weapon_input = tk.Entry(self.Simulator)   ####user's weapon input

        #weapon_input.bind('<Enter>' , enter_pressed)
        self.weapon_input.pack()


        #create listbox
        self.weapons_list = Listbox(self.Simulator , width = 50 , height = 5)
        self.weapons_list.pack()


        #pulls list of weapons user can select
        self.weapon_query = get_weapons()
        self.update(self.weapon_query)                  ####original location

        self.user_hit_chance = self.user_input('What is your total hit chance' , 60)

        self.user_crit_chance = self.user_input("What is your critical chance?" , 60)

        self.user_weapskill = self.user_input('What is your added weapon skill?' , 60)

        self.user_fight_duration = self.user_input('How long is your fight in seconds? (no longer than 6 minutes)' , 600 )

        self.user_iterations = self.user_input('Number of iterations:' , 200)

        #Create binding on entry box to autofill
        self.weapon_input.bind("<KeyRelease>" , self.check_listbox)

        #Listboxs = <<>> , single actions = <> , select from the listbox
        self.weapons_list.bind("<<ListboxSelect>>" , self.fillout)

        self.button = tk.Button(self.Simulator , text = "Begin Simulation" , command = lambda: self.button_action(self.weapon_input.get()))
        self.button.pack()

        
        self.Simulator.mainloop()




    #Update the listbox
    def update(self , weapon_query_1):
        #Clear the listbox
        self.weapons_list.delete(0 , END)
        #Add weapons to listbox
        # print(type(weapon_query_1))
        for items in weapon_query_1:
            # print(type(items))
            self.weapons_list.insert(0 , items)
            

    #update entry box with listbox click
    def fillout(self , event):
        #delete what is in in entry box
        self.weapon_input.delete(0 , END)
        #adds the click event from the user
        self.weapon_input.insert(0 , self.weapons_list.get(ACTIVE))


    #checks entry against the imported listbox  
    def check_listbox(self , event):
        #get what is user_input
        user_input = self.weapon_input.get()
        list_data = []
        if user_input == '':
            for weapon in self.weapon_query:
                list_data.append(weapon)
        else:
            for weapon in self.weapon_query:
                if user_input.lower() in weapon.lower():
                    list_data.append(weapon)

        #update listbox with selected item
        update(list_data)


    def user_input(self , label , max_box):
        input_label = tk.Label(self.Simulator , text = label )
        input_label.pack()
        spinbox_labeler = tk.Spinbox(self.Simulator , from_ = 0 , to_ = max_box)
        spinbox_labeler.pack()
        return spinbox_labeler


    def button_action(self , weapon_input):
        weapon_stats = get_weapon_stats(weapon_input)
        result = do_simulation( int(weapon_stats['dmg_min1']),
                                int(weapon_stats['dmg_max1']),
                                int(weapon_stats['delay'])/1000,
                                int(self.user_hit_chance.get()), int(self.user_crit_chance.get()),
                                int(self.user_weapskill.get()), int(self.user_iterations.get()))
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
        

Gui = WoWSimGui()