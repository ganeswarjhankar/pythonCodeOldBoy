from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
driver.get("https://www.hexahealth.com/ ")

Inputboxes=driver.find_elements_by_class_name()
Print (len(inputboxes)
