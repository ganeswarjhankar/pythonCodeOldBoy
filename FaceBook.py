

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
import time
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://www.facebook.com/")
#register Click
driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()

time.sleep(3)

driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("First Name Test check")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("test Sure Name")
driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys("Checkjhankar@yahoo.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Check Password")
driver.find_element(By.XPATH,"//input[@name='reg_email_confirmation__']").send_keys("check re-password")

Day = Select(driver.find_element(By.XPATH,"//select[@title='Day']"))
Day.select_by_visible_text("10")

Month = Select(driver.find_element(By.XPATH,"//select[@title='Month']"))
Month.select_by_visible_text("Jul")
Year = Select(driver.find_element(By.XPATH,"//select[@title='Year']"))
Year.select_by_visible_text("2022")
driver.find_element(By.XPATH,"//input[@id='u_x_4_3g']").click()


#month = driver.find_element_by_id("month")
#month = driver.find_element(By.ID,"month")

#driver.find_element(By.CSS_SELECTOR,"option[value='1']").click()

driver.close()


