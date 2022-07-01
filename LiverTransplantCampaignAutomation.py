from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select


import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)


URL=driver.get("https://hexahealth.com/campaigns/liver-transplant")
print("URL")
driver.maximize_window()
#scroll down for Pixel Method

#driver.execute_script("window.scrollBy(0,1500)","")
#driver.find_element(By.XPATH,"//*[@id='leadname5']").send_keys("Liver-Test Sanity-GJ")
#driver.find_element(By.XPATH,"//*[@id='contactnum5']").send_keys("1000000617")
#driver.find_element(By.XPATH,"//*[@id='LeadSubmit']").click()
time.sleep(5)

#driver.back()

Element = driver.find_element(By.XPATH,"//*[@id='surgerytBtn']/i")
driver.execute_script("arguments[0].click();",Element)

modal = driver.find_element(By.XPATH,"//*[@id='appointModalLabelsurgery']")
driver.execute_script("arguments[0].scrollIntoView();",modal)
driver.find_element(By.XPATH,"//*[@id='closemodal']").click()


driver.close()





#Appointment = driver.find_element(By.LINK_TEXT,("Get a free second opinion from top surgeons! Book an appointment »")).click()
#driver.find_element(By.XPATH,"//*[@id='leadname2']").send_keys("Form1_PatientName")
#driver.find_element(By.ID,"contactnum2").send_keys("7896544568")


#driver.switch_to.frame(driver.find_element(By.XPATH,"//*[@id='appointmodal']/div/div/div[2]"))
#driver.find_element(By.ID,"leadquery").send_keys("Form1_PatientName is  test")

#driver.find_element(By.XPATH,"//*[@id='closemodal']").click()

#time.sleep(5)




