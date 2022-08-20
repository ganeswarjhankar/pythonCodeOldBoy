from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.youtube.com/watch?v=r6AkPpn4PdQ&list=PLd3UqWTnYXOllYuWoZi2Uz27V7FzYZCdK&index=13")

driver.maximize_window()

time.sleep(10)

driver.find_element(By.XPATH,"//*[@id='video-title']").click()

