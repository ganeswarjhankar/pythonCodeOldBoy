from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

S=Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)

driver.get("http://stagingcms.hexahealth.com/")
driver.find_element(By.XPATH,"//*[@id='UserName']").send_keys("ganeswar.jhankar@hexahealth.com")

driver.find_element(By.XPATH,"//*[@id='Password']").send_keys("Hexa!234")
driver.find_element(By.XPATH,"//*[@id='btnLogin']").click()
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='drpAllForms']")