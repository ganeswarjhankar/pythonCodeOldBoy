#--time
import time
#--Selenium webdriver
from selenium import webdriver
#--Chrome Browser
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)
##---maximize the window
driver.maximize_window()
#driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.get("https://www.hexahealth.com")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@id='txtArticls']").send_keys("anu")
Image = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/img")
assert Image==
