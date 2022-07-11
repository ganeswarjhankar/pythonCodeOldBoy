from selenium import webdriver
#from selenium.webdriver import ActionChains
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
driver.implicitly_wait(10)

Doctor = Select(driver.find_element(By.XPATH,"//select[@id='drpAllForms']"))
Doctor.select_by_visible_text("1 - Doctor")

driver.implicitly_wait(10)
#create Doctor page

driver.find_element(By.XPATH,"//input[@placeholder='Enter Doctor Name']").send_keys("Doctor GJ test CMS Automation")
Gender = Select(driver.find_element(By.XPATH,"//select[@name='BasicInfo.Gender']"))
Gender.select_by_visible_text("Male")


driver.find_element(By.XPATH,"//input[@id='BasicInfo_AddressLine1']").send_keys("Address GJ test CMS Automation")


driver.find_element(By.XPATH,"//input[@id='BasicInfo_AddressLine2']").send_keys("Address GJ test CMS Automation")



driver.close()

