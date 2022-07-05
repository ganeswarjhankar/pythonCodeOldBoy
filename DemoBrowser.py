from selenium import webdriver
from selenium.webdriver.chrome.service import Service




service_obj = Service("D:\\chromedriver.exe");

driver = webdriver.Chrome(service=service_obj )

India = driver.get("https://indiatimes.com")
print(driver.title)
print(driver.capabilities)
print(driver.current_url)
google = driver.get("https://google.com")
#driver.maximize_window()
#driver.back()
#driver.forward()
#driver.refresh()

driver.minimize_window()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
else:
    print(India)

driver.close()  

