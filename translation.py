from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def translate(question, language):

    PATH = "./chromedriver"

    driver = webdriver.Chrome(PATH)

    if language == "english":
        driver.get(f"https://translate.google.com/?sl=auto&tl=en&text={question}&op=translate")

    elif language == "spanish":
        driver.get(f"https://translate.google.com/?sl=auto&tl=es&text={question}&op=translate")

    else:
        return None
    
    time.sleep(5)

    translation = driver.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span")

    return translation.text.lower()

