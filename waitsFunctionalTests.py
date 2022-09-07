from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains


import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.implicitly_wait(10)
# 5 secs is the MAX timeout..2 secs or 3 secs save


driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# results = driver.find_elements((By.XPATH,"(//div[@class='products'])[1]"))

count = len(results)
# always must give results so this is used
# chanining the process
assert count > 0
for x in results:
    x.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#sum Validation check for the Items

totals = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for total in totals:
    sum = sum + int(total.text)
print(sum)

totalAmount = int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)

print(totalAmount)


#compare the totalAmount and sum
assert sum==totalAmount







driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")

code = driver.find_element(By.XPATH, "//button[@class='promoBtn']")
code.click()


wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

print(code.text)

driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/button").click()

dropdown = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/select")
dropdownCountry = Select(dropdown)
#dropdownCountry.select_by_visible_text("Afghanistan")
#dropdownCountry.select_by_index()
dropdownCountry.select_by_value("Afghanistan")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(3)
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/button").click()







# for result in results:
# result.find_element(By.XPATH,"//div[@class='products']/div/div/button").click()

# time.sleep(2)

# driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()

# river.find_element(By.XPATH,"(//button[@type='button'])[1]").click()
