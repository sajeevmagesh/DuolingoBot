from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
time.sleep(7)
lesson="Travel"

driver.get(f"https://www.duolingo.com/skill/es/{lesson}/")
errors=[[]]

def question():
    submit_button=driver.find_element_by_class_name("_2orIw")
    question=driver.find_element_by_xpath("//h1[@class='_2LZl6']/span").text
    print(question)
    answer=""
    if "Which one of these is" in question:
        question=question.replace('Which one of these is ','')
        question=question[1:-1]
        question=question[:-1]
        answer=translate(question, "spanish")
        answer_choices=driver.find_elements_by_class_name("HaQTI")
        for x in range(len(answer_choices)):
<<<<<<< HEAD
<<<<<<< HEAD
            if answer==answer_choices[x].text.lower():
=======
            if answer==answer_choices[x].text:
>>>>>>> parent of af34ec9... I just made this program 10000% better
=======
            if answer==answer_choices[x].text:
>>>>>>> parent of af34ec9... I just made this program 10000% better
                answer_choices[x].click()
        submit_button.click()
        submit_button.click()
    elif "Write this in English" in question:
        keyboard=driver.find_element_by_class_name("_29cJe")
        keyboard.click()
        text_area=driver.find_element_by_class_name("_2EMUT")
        text_area.click()
        text_area.send_keys(answer)
        text_area.send_keys(Keys.ENTER)
    elif "Mark the correct meaning" in question:
        question=driver.find_element_by_class_name("_3-JBe").text
        print(question)
<<<<<<< HEAD
<<<<<<< HEAD
        answer=translate(question, "spanish")
        answer_choices=driver.find_elements_by_class_name("_2CuNz")
        for z in range(len(answer_choices)):
            if answer_choices[z].text.lower()==answer:
                answer_choices[z].click()
        submit_button.click()
        submit_button.click()
        
=======
>>>>>>> parent of af34ec9... I just made this program 10000% better
=======
>>>>>>> parent of af34ec9... I just made this program 10000% better
    elif "Write this in Spanish" in question:
        keyboard=driver.find_element_by_class_name("_29cJe")
        keyboard.click()
        text_area=driver.find_element_by_class_name("_2EMUT")
        text_area.click()
        text_area.send_keys(answer)
        text_area.send_keys(Keys.ENTER)
    else:
        skip=driver.find_element_by_class_name("J51YJ")
        skip.click()

def translate(question, language):
    secondwindow = webdriver.Chrome(PATH)
    if language == "english":
        secondwindow.get(f"https://translate.google.com/?sl=auto&tl=en&text={question}&op=translate")
    elif language == "spanish":
        secondwindow.get(f"https://translate.google.com/?sl=auto&tl=es&text={question}&op=translate")
    else:
        return None
    time.sleep(3.5)
    translation = secondwindow.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span")
    return translation.text.lower()
    secondwindow.quit()
question()
    
