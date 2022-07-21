import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


#driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.get("https://www.hexahealth.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"(//a[@href='/treatment/general-surgery-inguinal-hernia-surgery'])[4]").click()

time.sleep(5)
try:
    l= driver.find_element(By.TAG_NAME,"Oops!")
    s = l.text
    print("Element exist -" + s)
#NoSuchElementException thrown if not present
except NoSuchElementException:
    print("Element does not exist")
#driver.close()