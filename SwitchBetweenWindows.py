import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle)
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
time.sleep(5)
driver.quit()



#driver.window_handles