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
    question()
    question()
\
def question():
    time.sleep(1)
    correct_or_not = False
    answer=""
    try:
        tip=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span/span")
    except:
        tip=""
    if "Here's a tip" in tip:
        tip_button=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[8]/div/label[1]/div")
        tip_button.click()
        submit_button=driver.find_element_by_class_name("_2orIw")
        submit_button.click()
        return None
    
    try:
        question=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div[1]/h1/span").text
    except:
        submit_button=driver.find_element_by_class_name("_2orIw")
        submit_button.click()
        return None

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

def Write_this_in_English(question):
    keyboard=driver.find_element_by_class_name("yWRY8")
    print(keyboard.text)
    if keyboard.text.lower()=="use keyboard":
        keyboard.click()
    text_area=driver.find_element_by_class_name("_2EMUT")
    text_area.click()
    text_area=driver.find_element_by_class_name("_2EMUT")
    text_area.click()
    question2=driver.find_elements_by_class_name("_34k_q")
    for x in range(len(question2)):
        if x>0:
            question=question+" "+question2[x].text.lower()
        else:
            question=question2[x].text.lower()
    answer=translate(question,"english")
    text_area.send_keys(answer)
    text_area.send_keys(Keys.ENTER)
    submit_button=driver.find_element_by_class_name("_2orIw")
    submit_button.click()
    
def Mark_the_correct_meaning(question):
    question = driver.find_element_by_class_name("_3-JBe")
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
    
def Write_this_in_Spanish(question):
    keyboard=driver.find_element_by_class_name("yWRY8")
    print(keyboard.text)
    if keyboard.text.lower()=="use keyboard":
        keyboard.click()
    text_area=driver.find_element_by_class_name("_2EMUT")
    text_area.click()
    question2=driver.find_elements_by_class_name("_34k_q")
    for x in range(len(question2)):
        if x>0:
            question=question+" "+question2[x].text.lower()
        else:
            question=question2[x].text.lower()
    answer=translate(question,"spanish")
    text_area.send_keys(answer)
    text_area.send_keys(Keys.ENTER)
    submit_button=driver.find_element_by_class_name("_2orIw")
    submit_button.click()

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
    translation2=translation.text.lower()
    secondwindow.quit()
    return translation2



lesson("Intro")
    
