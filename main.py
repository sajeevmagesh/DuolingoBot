from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse
username="Test1234"
password="Test1234"
PATH = "./chromedriver"

driver=webdriver.Chrome(PATH)

##Duolingo Login
driver.get("https://www.duolingo.com/log-in?isLoggingIn=true")
parentform=driver.find_element_by_class_name("_3jeu0")
usernameform=driver.find_element_by_xpath("//div[@class='_3jeu0']/div[@class='_2a3s4']/label[@class='_2S_JP']/div[@class='_2rjZr']/input")
passwordform=driver.find_element_by_xpath("//div[@class='_3jeu0']/div[@class='_2a3s4'][position()=2]/label[@class='_2S_JP']/div[@class='_2rjZr']/input")
loginbtn=driver.find_element_by_class_name("_2oW4v")
usernameform.click()
usernameform.send_keys(username)
passwordform.click()
passwordform.send_keys(password)
loginbtn.click()

##Duolingo Lesson
driver.implicitly_wait(10)
time.sleep(10)
lesson="Intro"

driver.get(f"https://www.duolingo.com/skill/es/{lesson}/")
question=driver.find_element_by_xpath("//h1[@class='_2LZl6']/span").text
print(question)
if "Which one of these is" in question:
    question=question.replace('Which one of these is ','')
    question=question[1:-1]
    question=question[:-1]
    print(question)
try:
    keyboard=driver.find_element_by_class_name("_29cJe")
    keyboard.click()

except:
    pass

def translate(question, language):

    PATH = "./chromedriver"

    driver = webdriver.Chrome(PATH)

    if language == "english":
        driver.get(f"https://translate.google.com/?sl=auto&tl=en&text={question}&op=translate")

    elif language == "spanish":
        driver.get(f"https://translate.google.com/?sl=auto&tl=es&text={question}&op=translate")

    else:
        return None
    
    time.sleep(3.5)

    translation = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span")
    
    return translation.text.lower()

    driver.quit()

    