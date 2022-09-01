from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

Expected list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]


import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.implicitly_wait(10)
# 5 secs is the MAX timeout..2 secs or 3 secs save


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
