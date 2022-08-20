
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


driver.get("https://www.hexahealth.com/")


driver.maximize_window()


driver.find_element(By.XPATH,"//input[@id='txtArticls']").send_keys("Anu Jain")
time.sleep(3)
doctors = driver.find_elements(By.XPATH,"//li[@name='5articleIndex']")

time.sleep(5)

for anu in doctors:
    if anu.text=="Anu Jain":
        anu.click()
        break
value = driver.find_element(By.XPATH,"//input[@id='txtArticls']").get_attribute('value')
print(value)

assert value == "Anu Jain"






