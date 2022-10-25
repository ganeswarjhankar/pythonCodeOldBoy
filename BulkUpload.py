

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.action_chains import ActionChains
import time
#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.support.wait import WebDriverWait
S=Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)


URL=driver.get("https://httpstatus.io/")

driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section[2]/div/form/div[1]/div/p[1]/textarea").send_keys\
    ("https://hexahealth.com/marketing/SINUS_SURGERY")

driver.implicitly_wait(5)
#driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section[1]/div/form/div[2]/div/a").

driver.find_element(By.XPATH,"//button[@class='button']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section[2]/div/form/div[2]/div/a").click()

#Status = driver.find_element(By.XPATH,"//*[@id='results']/div/div[2]/div[3]/div/div[1]/table/tbody/tr/td[3]/div/span[2]")

try:
    wait = WebDriverWait(driver,1)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"200")))
    print("Passed")
except TimeoutException:
    print("waiting")




##SuccessText = driver.find_element(By.LINK_TEXT,"200").text


#assert  "Success! Thank you!" in SuccessText







