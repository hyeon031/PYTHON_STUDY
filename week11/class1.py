# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:13:26 2023

@author: ejrgi
"""

def basic():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path = ChromeDriverManager().install())
    browser = webdriver.Chrome(service = service, options = options)
    browser.get("https://www.google.com")
    
# basic()


# =============================================================================
# 다음 사이트 자동 로그인 & 로그아웃
# =============================================================================

def test1():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    import time
    import pyperclip
    import pyautogui
    
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path = ChromeDriverManager().install())
    browser = webdriver.Chrome(service = service, options = options)
    
    browser.implicitly_wait(5)
    browser.get("https://www.daum.net/")
    
    # 로그인
    
    #inner_login > a.link_login.link_kakaoid
    
    browser.find_element(By.CSS_SELECTOR,"#inner_login > a").click()
    browser.find_element(By.CSS_SELECTOR,"#loginId--1").click()
    time.sleep(1)
    pyperclip.copy('01082088131')
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    
    #password--2
    
    browser.find_element(By.CSS_SELECTOR,"#password--2").click()
    time.sleep(1)
    pyperclip.copy("abcde")
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    
    browser.find_element(By.CSS_SELECTOR, "#mainContent > div > div > form > div.confirm_btn > button.btn_g.highlight.submit").click()
    
# test1()


# =============================================================================
# 네이버 쇼핑몰 크롤링
# =============================================================================


def test2():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    
    import time
    import pyautogui
    import pyperclip
    from selenium.webdriver.common.keys import Keys
    
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path = ChromeDriverManager().install())
    browser = webdriver.Chrome(service = service, options = options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get("https://naver.com/")
    
    # 접속
    # browser.find_element(By.CSS_SELECTOR,"#shortcutArea > ul > li:nth-child(4) > a > span.service_icon.type_shopping").click()
    url = browser.find_element(By.CSS_SELECTOR,"#shortcutArea > ul > li:nth-child(4) > a").get_attribute("href")
    browser.close()
    
    #새로운 브라우저를 띄움.
    browser = webdriver.Chrome(service = service, options=options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get(url)
    
    # 탐색
    
    browser.find_element(By.CSS_SELECTOR, "#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div._searchInput_search_input_QXUFf > input").click()
    time.sleep(1)
    pyperclip.copy("오메가3")
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR,"#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div._searchInput_search_input_QXUFf > button._searchInput_button_search_1n1aw > svg > path").click()
    
    # 스크롤
    
    before = browser.execute_script("return window.scrollY")
    
    while(True):
        browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        time.sleep(1)
        after = browser.execute_script("return window.scrollY")
        
        if before == after:
            break
        before = after
        
    
test2()








