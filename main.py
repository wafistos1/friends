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
from package.subscene import get_subtitle_opensub



options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"/home/wafi/Downloads/toto",# link of Download files
  "download.directory_upgrade":True,
  "safebrowsing.enabled":True,
  "download.prompt_for_download":False,
})
driver=webdriver.Chrome(options=options)
#driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\ChromeDriver\chromedriver_win32\chromedriver.exe')


print('**************************************************')
print('**************************************************')
print('**************************************************')
print('**************************************************')
print('********** Download subtitle Programme ***********')
print('**************************************************')
print('**************************************************')
print('**************************************************')
print('**************************************************')


print('Welcome ....')
print('Choose the site you want')
print()
page_num = int(input('\nEnter number of page 1-10: '))
down_num = int(input('\nEnter number of downlaod files: '))




get_subtitle_opensub(driver, page_num, down_num)
