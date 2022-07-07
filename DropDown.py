from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#control = driver.find_element(By.CLASS_NAME, "form-control")
#dropdown = Select().select_by_visible_text



#select * from check to push button

#static dropdown

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_visible_text("Female")
 







