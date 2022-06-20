
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select

import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.hexahealth.com/")
print("URL")
driver.maximize_window()
#scroll down for Pixel Method

#driver.execute_script("window.scrollBy(0,3100)","")

 #Scroll down page till the element is visible
Consultation = driver.find_element(By.CLASS_NAME,"consultation-form")
driver.execute_script("arguments[0].scrollIntoView();",Consultation)
driver.find_element(By.CLASS_NAME,"form-control").send_keys("TestCheck")
driver.find_element(By.CSS_SELECTOR,"input[id='contactnumhome']").send_keys("9438857617")

#DropDown = Select(driver.find_element(By.ID,""))

time.sleep(5)
Consultation1 = driver.find_element(By.CLASS_NAME,"btn-round-primary")
driver.execute_script("arguments[0].scrollIntoView();",Consultation1)

driver.find_element(By.CSS_SELECTOR,"input[id='contactnum1']").send_keys("9438857617")

#Delhi=driver.find_element(By.CSS_SELECTOR,"input[text=' Delhi - NCR']")

time.sleep(5)


driver.close()



