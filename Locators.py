
from selenium .webdriver.common.by import By
import time



from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://hexahealth.com/marketing/knee-replacement-bangalore")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"form-control").send_keys("GJ Test AUTOMATE")
driver.find_element(By.ID,"contactnum5").send_keys("9438857617")
driver.find_element(By.CSS_SELECTOR,"option[value='1']").click()
time.sleep(3)

driver.close()

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://hexahealth.com/campaigns/varicoseveins")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"form-control").send_keys("GJ Test AUTOMATE")

driver.find_element(By.ID,"contactnum5").send_keys("9438857617")
##driver.find_element(By.CSS_SELECTOR,"option[value='1']").click()


time.sleep(3)
driver.close()

##Driver.execute_script(“arguments[0].scrollIntoView();”,)







