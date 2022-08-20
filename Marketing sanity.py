from selenium import webdriver
from selenium.webdriver.chrome.service import Service


S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)

URL= driver.get("https://www.google.com/")

