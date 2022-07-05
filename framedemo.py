from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time


S=Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame()
driver.find_element(By.CLASS_NAME,"mce-content-body ").clear()
driver.find_element(By.CLASS_NAME,"mce-content-body ").send_keys("I am unable to find Elements")
#switch to the main frame
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,"h3").text)



