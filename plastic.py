

from os import remove
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chromium.webdriver import ChromiumDriver

from selenium.common.exceptions import NoSuchElementException,UnexpectedAlertPresentException

CONFIG = {'建威':'N000151034:AAQQx123','宇翔':'N000151034:AAQQw123','美樺':'N000151034:AAQQw123'}
WEBSITE = "https://{}@cloud.fpcetg.com.tw/FPG/WEB/COM/TTS/Default.aspx"


def doAutoTyping(data:dict):
    driver = webdriver.Chrome()
    driver.execute_script
    __doLogin(driver , data)

    try:
        if(data['mode'] == "開始練習"):
            __doPracticing(driver,data)
        # else if(data['mode'] == "開始測驗"):
    except UnexpectedAlertPresentException:
        
        print("UnexpectedAlertPresentException")
    
    input('Enter to Stop')


def __doLogin(driver:ChromiumDriver , data:dict ):   
    driver.get(WEBSITE.format(CONFIG[ data['user'] ]))

def __doTesting(driver:ChromiumDriver):
    
    driver.execute_script("goUrl('Default.aspx');") 
    Select(driver.find_element("id", "Ddl_Time")).select_by_index(2)

def __doPracticing(driver:ChromiumDriver , data:dict ):

    driver.execute_script("goUrl('Default.aspx');") 
    Select(driver.find_element("id", "Ddl_Time")).select_by_index( data['practiceTime'] )


    driver.find_element("id", "btn_Practice").click()

    time.sleep(5)

    driver.execute_script("__doPostBack('btn_modal_Save','')")

    time.sleep(5)

    question_words = driver.find_element("id", "Tb_Value").text

    
    answer = driver.find_element("id", "Tb_Answer")
    for word in question_words:                
        answer.send_keys(word)
        pyautogui.press('right')

    driver.execute_script("__doPostBack('btn_Save','')")












