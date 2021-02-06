from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = "Test123"
password = "Test123"

PATH = "chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://www.duolingo.com/log-in?isLoggingIn=true")

time.sleep(10)

username_and_password = driver.find_element_by_class_name("_3MNft fs-exclude")

for i in username_and_password:
    i.send_keys("Test123")



