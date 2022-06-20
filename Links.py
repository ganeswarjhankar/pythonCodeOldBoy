from selenium import webdriver
from selenium .webdriver.common.by import By

#S=Service("D:\\chromedriver.exe")
#driver=webdriver.Chrome(service=S)

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()
Links=driver.find_elements(By.TAG_NAME,"i")
print("Number of links:",len(Links))

for link in Links:
    print(link.text)

    #clicking on the link
driver.find_element(By.PARTIAL_LINK_TEXT,"REG")


