import MySQLdb
import pandas as pd
import MySQLdb.cursors

#close DB at some point
db = MySQLdb.connect(host ='localhost', user='root', passwd='password',db='wow_db', cursorclass = MySQLdb.cursors.DictCursor)

cur = db.cursor()

# query = """SELECT entry,name,dmg_min2,dmg_max2,sheath FROM wow_db.item_template where sheath > 0 and name = %s"""
query = "SELECT name FROM wow_db.item_template where sheath > 0"

# user_input = "Lupine Axe"
def get_weapons():
    cur.execute(query)
    weapons = cur.fetchall()

    # print(len(weapon))
    names = []
    for weapon in weapons:
        names.append(weapon["name"])

    return names

# shortcut to the above function return
# return [weapon["name"] for weapon in weapons]


