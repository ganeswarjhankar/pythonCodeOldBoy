from selenium import webdriver
from selenium .webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="D:\\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

#driver.find_element_by_xpath("//*[@id="HTML9"]/div[1]/button").Click()
#driver.find_element(By.XPATH , "//*[@id='HTML9]'/div[1]/button").Click()
driver.find_element(By.CSS_SELECTOR,"button[onclick='myFunction()']").click()

time.sleep(5)
print(Alert.text)
#Alert=driver.switch_to.alert.accept()


Alert = driver.switch_to.alert.dismiss()
