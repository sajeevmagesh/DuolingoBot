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

time.sleep(7)

def lesson(lesson):
    driver.get(f"https://www.duolingo.com/skill/es/{lesson}/")
    time.sleep(3.5)
    question()
    time.sleep(30)
    question()

def question():
    correct_or_not = False
    answer=""
    question=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div[1]/h1/span").text
    if "Which one of these is" in question:
        Which_one_of_these_is(question)
    elif "Write this in English" in question:
        Write_this_in_English(question)
    elif "Mark the correct meaning" in question:
        Mark_the_correct_meaning(question)
    elif "Write this in Spanish" in question:
        Write_this_in_Spanish(question)
    else:
        skip=driver.find_element_by_class_name("J51YJ")
        skip.click()

def Which_one_of_these_is(question):
    question=question.replace('Which one of these is ','')
    question=question[1:-1]
    question=question[:-1]
    answer=translate(question, "spanish")
    answer_choices=driver.find_elements_by_class_name("HaQTI")
    for x in range(len(answer_choices)):
        if answer==answer_choices[x].text:
            answer_choices[x].click()
            correct_or_not = True
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            submit_button.click()
    return correct_or_not

def Write_this_in_English():
    keyboard=driver.find_element_by_class_name("_29cJe")
    keyboard.click()
    text_area=driver.find_element_by_class_name("_2EMUT")
    text_area.click()
    
    text_area.send_keys(answer)
    text_area.send_keys(Keys.ENTER)
    
def Mark_the_correct_meaning(question):
    question = driver.find_element_by_class_name("_3-JBe")
    if translate(question.text, "spanish") == question:
        translation = translate(question.text, "english")
    else:
        translation = translate(question.text, "spanish")
    answers = driver.find_elements_by_class_name("_2CuNz")
    for i in answers:
        if i.text.lower() == translation:
            i.click()
            correct_or_not = True
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            submit_button.click()
    return correct_or_not
    
def Write_this_in_Spanish():
    keyboard=driver.find_element_by_class_name("_29cJe")
    keyboard.click()
    text_area=driver.find_element_by_class_name("_2EMUT")
    text_area.click()
    text_area.send_keys(answer)
    text_area.send_keys(Keys.ENTER)

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
    secondwindow.quit()
    return translation.text.lower()
    


lesson("Intro")