import MySQLdb
import pandas as pd
import MySQLdb.cursors

#close DB at some point
db = MySQLdb.connect(host ='localhost', user='root', passwd='password', db='wow_db', cursorclass = MySQLdb.cursors.DictCursor)

cur = db.cursor()



# user_input = "Lupine Axe"
def get_weapons():
    # query = """SELECT entry,name,dmg_min2,dmg_max2,sheath FROM wow_db.item_template where sheath > 0 and name = %s"""
    query = "SELECT entry,name,dmg_min1,dmg_max1,sheath FROM wow_db.item_template where sheath != 0 and sheath != 4 ORDER BY name DESC"
    cur.execute(query)
    weapons = cur.fetchall()
    
    names = []
    for weapon in weapons:
        names.append(weapon["name"])

    return names


def get_weapon_stats(weapon_name):
    query = "SELECT dmg_min1,dmg_max1,delay FROM wow_db.item_template where name = %s "
    cur.execute(query , (weapon_name,))
    
    return cur.fetchone()


# def weapon_dmg():
#     cur.execute(query)
#     minimum_damage = cur.fetchall()

#     mindmg = []
#     for minimum in minimum_damage:
#         mindmg.append(minimum_damage["dmg_min1"])
    
#     return names


# shortcut to the above function return
# return [weapon["name"] for weapon in weapons]


