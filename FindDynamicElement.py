import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

 # select the auto search
driver.find_element(By.XPATH,"//input[@id='autosuggest']").send_keys("ind")
time.sleep(5)
search = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
print(len(search))

for country in search:
    if country.text =="India":
        country.click()
        break

print(driver.find_element(By.XPATH,"//input[@id='autosuggest']").text)

