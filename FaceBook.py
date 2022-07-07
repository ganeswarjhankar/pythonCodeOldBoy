from selenium import webdriver
from .select import Select
#from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#import time
driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
#S=Service("D:\\chromedriver.exe")
#driver=webdriver.Chrome(service=S)
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()
month = driver.find_element(By.ID,"month")
monthDD = Select(month)
monthDD.select_by_visible_text("Jul")





#driver.close()


