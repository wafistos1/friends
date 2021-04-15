#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import re
from selenium.webdriver.common.action_chains import ActionChains
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options











def get_subtitle_opensub(driver, page_num, file_num):
    #Create driver
    driver.get("https://subscene.com/browse/latest/film/1")

    link_list = []
    # click filter button
    filter_btn = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/small/a')
    filter_btn.click()
    time.sleep(5)

    #click arabic checkbox
    filter_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div/form/div[1]/div[1]/label/input')
    filter_btn.click()
    time.sleep(5)

    print('Arabic selected Ok')
    #click Save changes
    filter_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div/form/div[2]/button')
    filter_btn.click()
    time.sleep(5)
    print('Filter seldcted Ok')


    #Forloop all movies with arabic substitle
    for i in range(1, page_num):
        driver.get(f"https://subscene.com/browse/latest/film/{i}")
        time.sleep(5)
        #Search all href in page
        links = driver.find_elements_by_tag_name('a')
        my_regex_pattern = r"https://subscene.com/subtitles/(?P<title>[\w-]+)/(?P<language>[\w-]+)/(?P<product_id>[\w-]+)"
        regex = re.compile(my_regex_pattern)
        for lin in links:
            try:
                my_match = regex.match(lin.get_attribute('href'))
                if my_match != None and my_match['language'] == 'arabic':
                    link_list.append(lin.get_attribute('href'))
            except:
                pass
    print(f'You can download  {len(link_list)} Files') 

    #download files
    for list in link_list[:file_num]:
        driver.get(list)
        driver.implicitly_wait(10) # seconds
        
        # Ajouter l'affichage du titre dans la console
        search = driver.find_element_by_id('downloadButton')
        search.click()
        time.sleep(3)

    # End
    driver.quit()
    print('All files are now download')
    print('Bye...')