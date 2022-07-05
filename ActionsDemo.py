from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select


import time

S=Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.click_and_hold()
#action.context_click()
#action.double_click(driver.find_element())
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()



#driver.close()

