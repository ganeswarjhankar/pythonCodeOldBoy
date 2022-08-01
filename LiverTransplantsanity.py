from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.hexahealth.com/campaigns/liver-transplant")

driver.maximize_window()

driver.find_element(By.XPATH,"//i[@class='icon las la-calendar']").click()
time.sleep(3)
#driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("Patient check LT test")

driver.find_element(By.XPATH,"//*[@id='closemodal']/span").click()