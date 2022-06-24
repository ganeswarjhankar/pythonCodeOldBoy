from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)


Search = input("Enter the topic in the google for which you want to search")
