from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium .webdriver.common.by import By
#from selenium.webdriver.support.ui import Select

import time

S=Service("D:\\chromedriver.exe")
driver=webdriver.Chrome(service=S)