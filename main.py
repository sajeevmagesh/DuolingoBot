#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import urllib.parse
username="test1234"
password="test1234"
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
correct_or_not = False

time.sleep(7)
errors=[]
def lesson(lesson):
    driver.get(f"https://www.duolingo.com/skill/es/{lesson}/")
    while True:
        time.sleep(7)
        question()
        end_check=driver.find_elements_by_class_name("_2XF-t")
        if len(end_check)>0:
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            try:
                submit_button.click()
            except:
                pass
            try:
                submit_button.click()
            except:
                pass
            
            try:
                submit_button.click()
            except:
                pass
            try:
                submit_button.click()
            except:
                pass
            try:
                submit_button.click()
            except:
                pass
            break

def question():
    time.sleep(1)
    correct_or_not = False
    answer=""
    try:
        tip=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/span/span")
    except:
        tip=""
    if tip!="":
        if "here's a tip" == tip.text.lower():
            tip_button=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div/div[8]/div/label[1]/div")
            tip_button.click()
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            correct_or_not = True
            return None
    try:
        question=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/div/div/div/div/div[1]/h1/span").text

        
    except:
        try:
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            correct_or_not = True
            return None
        except:
            return None
    if "Which one of these is" in question:
        Which_one_of_these_is(question)
    elif "Write this in English" in question:
        Write_this_in_English(question)
    elif "Mark the correct meaning" in question:
        Mark_the_correct_meaning(question)
    elif "Write this in Spanish" in question or "Complete the translation" in question:
        Write_this_in_Spanish(question)
    else:
        skip=driver.find_element_by_class_name("J51YJ")
        skip.click()
        submit_button=driver.find_element_by_class_name("_2orIw")
        submit_button.click()

def Which_one_of_these_is(question):
    trueanswer=""
    correct_or_not=False
    question=question.replace('Which one of these is ','')
    question=question[1:-1]
    question=question[:-1]
    answer=translate(question, "spanish")
    for x in range(len(errors)):
        if question==errors[x][0]:
            answer=errors[x][1]
    answer_choices=driver.find_elements_by_class_name("HaQTI")
    for x in range(len(answer_choices)):
        if answer.lower()==answer_choices[x].text.lower():
            answer_choices[x].click()
            correct_or_not = True
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            submit_button.click()
    if correct_or_not == False:
        skip=driver.find_element_by_class_name("J51YJ")
        skip.click()
    try:
        is_correct=driver.find_element_by_class_name("_1x6Dk")
        if "Another correct solution:" == is_correct:
            pass
        else:
            trueanswer=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div").text
    except:
        pass
    if correct_or_not == False:
        errors.append([question, trueanswer])
        submit_button=driver.find_element_by_class_name("_2orIw")
        submit_button.click()
    return correct_or_not

def Write_this_in_English(question):
    trueanswer=""
    correct_or_not=False
    try:
        keyboard=driver.find_element_by_class_name("yWRY8")
        print(keyboard.text)
        if keyboard.text.lower()=="use keyboard":
            keyboard.click()
    except:
        pass
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
    for x in range(len(errors)):
        if question==errors[x][0]:
            answer=errors[x][1]
    text_area.send_keys(answer)
    text_area.send_keys(Keys.ENTER)
    incorrect=driver.find_elements_by_class_name("OLn6a")
    if len(incorrect)<1:
        correct_or_not=True
    try:
        is_correct=driver.find_element_by_class_name("_1x6Dk")
        if "Another correct solution:" == is_correct:
            pass
        else:
            trueanswer=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div").text
    except:
        pass
    if correct_or_not == False:
        errors.append([question, trueanswer])
    submit_button=driver.find_element_by_class_name("_2orIw")
    submit_button.click()
    
def Mark_the_correct_meaning(question):
    trueanswer=""
    correct_or_not=False
    question = driver.find_element_by_class_name("_3-JBe")
    translation = translate(question.text, "spanish")
    for x in range(len(errors)):
        if question.text==errors[x][0]:
            translation=errors[x][1]
    print(errors,translation)
    answers = driver.find_elements_by_class_name("_2CuNz")
    for i in answers:
        if i.text.lower() == translation.lower():
            i.click()
            correct_or_not = True
            submit_button=driver.find_element_by_class_name("_2orIw")
            submit_button.click()
            submit_button.click()
    if correct_or_not == False:
        skip=driver.find_element_by_class_name("J51YJ")
        skip.click()
    try:
        is_correct=driver.find_element_by_class_name("_1x6Dk")
        print(is_correct.text)
        if "Another correct solution:" == is_correct.text:
            pass
        else:
            trueanswer=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div").text
    except:
        pass
    if correct_or_not == False:
        errors.append([question.text, trueanswer])
        submit_button=driver.find_element_by_class_name("_2orIw")
        submit_button.click()
    return correct_or_not
    
def Write_this_in_Spanish(question):
    trueanswer=""
    correct_or_not=False
    try:
        keyboard=driver.find_element_by_class_name("yWRY8")
        print(keyboard.text)
        if keyboard.text.lower()=="use keyboard" or keyboard.text.lower()=="make harder":
            keyboard.click()
    except:
        pass
    text_area=driver.find_element_by_class_name("_2EMUT")
    text_area.click()
    question2=driver.find_elements_by_class_name("_34k_q")
    for x in range(len(question2)):
        if x>0:
            question=question+" "+question2[x].text.lower()
        else:
            question=question2[x].text.lower()
    answer=translate(question,"spanish")
    for x in range(len(errors)):
        if question==errors[x][0]:
            answer=errors[x][1]
    text_area.send_keys(answer)
    text_area.send_keys(Keys.ENTER)
    incorrect=driver.find_elements_by_class_name("OLn6a")
    if len(incorrect)<1:
        correct_or_not=True
    try:
        is_correct=driver.find_element_by_class_name("_1x6Dk")
        print(is_correct.text)
        if "Another correct solution:" == is_correct.text:
            pass
        else:
            trueanswer=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[3]/div/div/div[1]/div/div[2]/div[1]/div/div").text
    except:
        pass
    if correct_or_not == False:
        errors.append([question, trueanswer])


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
    translation = secondwindow.find_element_by_class_name("VIiyi")
    try:
        translation = secondwindow.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div[2]/div[1]/span[1]")
    except:
        pass
    translation2=translation.text.lower()
    secondwindow.quit()
    return translation2




   

lesson("Routines-2")
lesson("Community-2")
lesson("Community-2")
lesson("Community-2")
lesson("Community-2")

