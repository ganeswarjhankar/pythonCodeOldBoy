from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://hexahealth.com/marketing/lasik-bangalore")

driver.maximize_window()

driver.find_element(By.XPATH,"//input [@id='leadname5']").send_keys("Marketing Test Check")
driver.find_element(By.XPATH,"//input [@id='contactnum5']").send_keys("1000000001")
#driver.find_element(By.XPATH,"//button [@id='LeadSubmit']").click()

time.sleep(3)

#driver.back()

button = driver.find_element(By.XPATH,"//a[@id='surgerytBtn']")

driver.execute_script("arguments[0].click();", button)

time.sleep(3)

driver.find_element(By.XPATH,"//button[@id='headerCityClose']").click()

time.sleep(3)









