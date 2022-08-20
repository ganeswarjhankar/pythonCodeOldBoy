
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("berr")
time.sleep(5)



results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
#results = driver.find_elements((By.XPATH,"(//div[@class='products'])[1]"))

count = len(results)
assert count > 0




for result in results:
    result.find_element(By.XPATH,"//div[@class='products']/div/div/button").click()

time.sleep(2)

driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()

driver.find_element(By.XPATH,"(//button[@type='button'])[1]").click()














