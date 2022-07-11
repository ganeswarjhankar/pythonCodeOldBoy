
from selenium import webdriver
#brower exposes and executable file
#through selenium test we need to invoke the executable file which will then Invoke actual Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice//") #get method to hit url on browser
print(driver.title)
print(driver.current_url)

driver.find_element_by_css_selector("input[name='name']").send_keys("Test Successful")
driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys("Test ")
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys("Test Successful")
driver.find_element_by_xpath("//input[@id='exampleCheck1']").send_keys("Teste")
driver.find_element_by_xpath("//input[@id='inlineRadio1']").send_keys("Test Susful")

driver.find_element_by_xpath("//option[@value='1']").click()
#driver.find_element_by_xpath("//input[@id='inlineRadio3']").send_keys("TeSuccessful")
driver.find_element_by_xpath("//input[@type='submit']").click()


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


