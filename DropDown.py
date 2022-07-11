from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

S = Service("d:/chromedriver.exe")
driver = webdriver.Chrome(service=S)


driver.get("https://www.rahulshettyacademy.com/angularpractice/")

dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.close()

# select by value
#dropdown.select_by_value('1')




#select * from check to push button

#static dropdown

#dropdown.select_by_visible_text("Male")
#dropdown.select_by_visible_text("Female")
 







