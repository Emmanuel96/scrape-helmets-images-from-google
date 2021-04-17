import os
import json 
import requests
import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import base64
import time
import urllib.request

DRIVER_PATH = '/usr/local/bin/chromedriver'

SAVE_FOLDER = 'Helmets_classifier/helmet_images/'

GOOGLE_IMAGES = 'https://www.google.com/search?q=hardhat&rlz=1C5CHFA_enGB937GB937&sxsrf=ALeKk02twWeFWJCESdRh27hZxC0iZwBS6w:1617724623722&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiu0ans_envAhUkT98KHZ7CDiMQ_AUoAXoECAEQAw&biw=714&bih=732'


driver = webdriver.Chrome(DRIVER_PATH)
driver.get(GOOGLE_IMAGES)


# Scroll to the end of the page
def scroll_to_end():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    print('scroll done')

counter = 0
for i in range(1,10):     
    scroll_to_end()
    image_elements = driver.find_elements_by_class_name('rg_i')
    print(len(image_elements))
    for image in image_elements: 
        if (image.get_attribute('src') is not None):
            my_image = image.get_attribute('src').split('data:image/jpeg;base64,')
            filename = SAVE_FOLDER + 'helmet'+str(counter)+'.jpeg'
            if(len(my_image) >1): 
                with open(filename, 'wb') as f: 
                    f.write(base64.b64decode(my_image[1]))
            else: 
                print(image.get_attribute('src'))
                urllib.request.urlretrieve(image.get_attribute('src'), SAVE_FOLDER + 'helmet'+ str(counter)+'.jpeg')
            counter += 1
