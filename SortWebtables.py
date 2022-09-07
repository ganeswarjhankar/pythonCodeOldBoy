from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains


import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.maximize_window()
#Click on column header

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()


#Collect all the veggie names->>BrowserSortedveggielist (A,B,C)

driver.find_elements(By.XPATH,"//tr/td[1]")

#Sort this BrowserSortedveggielist -> newsortedlist ->(A,B,C)
#BrowserSortedveggielist == newsortedlist (Assert)
