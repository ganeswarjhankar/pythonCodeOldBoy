
#from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)



driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH , "/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Name Test Check demo")
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("Ganeswarjhankar@gmail.com")
driver.find_element(By.XPATH,"//*[@id='exampleInputPassword1']").send_keys("Password check")
#driver.find_element(By.XPATH,"//*[@id='exampleCheck1']").click()
#static drop down
sel = driver.find_element(By.XPATH,"//*[@id='exampleFormControlSelect1']").click()
dropdown = Select("sel")
dropdown = Select.select_by_visible_text









driver.close()
