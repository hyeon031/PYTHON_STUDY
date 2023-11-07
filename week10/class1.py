# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:35:09 2023

@author: ejrgi
"""

def test1():
    from selenium import webdriver
    browser = webdriver.Chrome()
    url = "https://www.chrome.com"
    browser.get(url)
    
# test1()


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


def test2():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path = ChromeDriverManager().install())
    browser = webdriver.Chrome(service = service, options = options)
    browser.get("https://www.naver.com")
    
    
    # shortcutArea > ul > li
    item_list = browser.find_elements(By.CSS_SELECTOR, "#shortcutArea > ul > li")
    # print(len(item_list))
    
    menu_item_list = []
    for item in item_list:
        try:
            # print(item.find_element(By.CSS_SELECTOR, "span.service_name").text)
            menu_item_list.append(item.find_element(By.CSS_SELECTOR, "span.service_name").text)
        except:
            # print("")
            menu_item_list.append("")
    
            
    print("기본메뉴 \n",menu_item_list)
    #shortcutArea > ul > li:nth-child(10) > a
    menu_item_list_ext = []
    browser.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(10) > a").click()
    
    
    # browser = browser.find_element(By.CSS_SELECTOR, "#shortcutArea > div > ul").text
    # print(browser)
    
    
    item_list = browser.find_elements(By.CSS_SELECTOR, "#shortcutArea > div > ul > li")
    for item in item_list:
        print(item.find_element(By.CSS_SELECTOR, "a").text)
        menu_item_list_ext.append(item.find_element(By.CSS_SELECTOR,"a").text)
        
    print("확장메뉴 \n", menu_item_list_ext)    
    
# test2()


# =============================================================================
# 네이버 자동 로그인(X), 봇을 인식함.
# =============================================================================

def test3():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path = ChromeDriverManager().install())
    browser = webdriver.Chrome(service = service, options = options)
    
    # 로그인 페이지로 이동
    
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
    
    # ID
    id = browser.find_element(By.CSS_SELECTOR, "#id")
    id.click()
    id.send_keys("GyuHyeon")
    
    # PW
    pwd = browser.find_element(By.CSS_SELECTOR, "#pw")
    pwd.click()
    pwd.send_keys("abcd12345")
    
    #로그인 버튼 클릭
    # log\.login
    
    btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
    btn.click()
    
    
# test3()



# =============================================================================
# 네이버 자동 로그인(X), 봇을 인식함.
# =============================================================================

def test4():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    
    import time
    import pyautogui
    import pyperclip
    
    options = Options()
    options.add_experimental_option("detach", True)
    service = Service(executable_path = ChromeDriverManager().install())
    browser = webdriver.Chrome(service = service, options = options)
    
    # 로그인 페이지로 이동
    
    browser.implicitly_wait(10)
    browser.maximize_window()
    browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
    
    # ID
    id = browser.find_element(By.CSS_SELECTOR, "#id")
    id.click()
    time.sleep(1)
    pyperclip.copy("5413cnrrntjs")
    pyautogui.hotkey("ctrl", 'v')
    time.sleep(2)
    
    # id.send_keys("GyuHyeon")
    
    # PW
    pwd = browser.find_element(By.CSS_SELECTOR, "#pw")
    pwd.click()
    time.sleep(1)
    pyperclip.copy("LCsolhe8131qnp@")
    pyautogui.hotkey("ctrl",'v')
    time.sleep(2)
    
    
    # pwd.send_keys("abcd12345")
    
    #로그인 버튼 클릭
    # log\.login
    btn = browser.find_element(By.CSS_SELECTOR,"#log\.login")
    btn.click()
    
    
test4()
