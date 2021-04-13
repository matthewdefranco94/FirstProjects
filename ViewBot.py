#view bot

import time
import random
from selenium import webdriver

#time to refresh page
time = random.randint(3 , 25)

link = 'https://www.youtube.com/watch?v=nb2IUfQyWG0'

number_of_views = 10

driver = webdriver.Chrome()
driver.get(link)

for i in range(number_of_views):
    time.sleep(time)
    driver.refresh()
