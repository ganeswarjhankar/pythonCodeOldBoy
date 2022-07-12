from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://www.hexahealth.com/")

driver.maximize_window()


driver.find_element(By.LINK_TEXT,("Get a free second opinion from top surgeons! Book an appointment »")).click()

driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//input[@id='leadname2']").send_keys("Patient test Name check")

driver.find_element(By.XPATH,"//input[@id='contactnum2']").send_keys("1000000001")

City = Select(driver.find_element(By.XPATH,"//select[@id='leadcity2']"))
City.select_by_visible_text( "Delhi - NCR")
driver.find_element(By.XPATH,"//textarea[@id='leadquery']").send_keys("test check")

#driver.find_element(By.XPATH,"//button[@id='LeadSubmitNewHome']").send_keys("Submit check")


time.sleep(3)
driver.find_element(By.XPATH,"//button[@id='closemodal']").click()
#driver.back()



driver.find_element(By.XPATH,"//input[@id='leadnamehome']").send_keys("Fold-2 Test Check" )
driver.find_element(By.XPATH,"//input[@id='contactnumhome']").send_keys("1000000001")

City2 = Select(driver.find_element(By.XPATH,"//select[@id='leadcityhome']"))
City2.select_by_visible_text("Delhi - NCR")

driver.find_element(By.XPATH,"//textarea[@id='leadqueryhome']").send_keys("test checck")


driver.find_element(By.XPATH,"//i[@class='las la-bars mobile-navigation']").click()



#print(driver.find_elements_by_class_name("alert alert-success alert-dismissible").text)






##login_form = driver.find_element(By.XPATH, "/html/body/form[1]")
##wait = WebDriverWait(driver, 100)
#driver.implicitly_wait(10)
#driver.back()
##driver.close()




#driver.back()
#driver.refresh()
#wait = WebDriverWait(driver, 110)
#driver.close()


