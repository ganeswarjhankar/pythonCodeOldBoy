from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support.ui import Select
from selenium .webdriver.common.by import By
import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

driver.get("https://www.facebook.com/")

driver.find_element(By.ID,"u_0_0_ks").click()

