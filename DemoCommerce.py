from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://demo.nopcommerce.com")
driver.implicitly_wait(3)
driver.maximize_window()
register = driver.find_elements(By.CSS_SELECTOR,"<a")
number = len(register)
print(number)
