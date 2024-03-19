import os
import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def new_window(brauser, old_windows):
    new_windows=brauser.window_handles
    wait=WebDriverWait(brauser, 30)
    wait.until(lambda d:len(old_windows) < len(new_windows))
    new_windows=old_windows-new_windows
    return new_windows

brauser=webdriver.Chrome()
brauser.implicitly_wait(0)

brauser.get('http://localhost/litecart/admin/?app=countries&doc=countries')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/?app=countries&doc=countries')

Newcountry=brauser.find_element(By.XPATH,"//a[text()=' Add New Country']").click()

Elements=brauser.find_elements(By.CSS_SELECTOR,"form[method='post'] a[target='_blank']")
for i in range(len(Elements)):
    elem=brauser.find_elements(By.CSS_SELECTOR,"form[method='post'] a[target='_blank']")

    elem[i].click()
    main_str=brauser.current_window_handle
    print(main_str)
    vse=brauser.window_handles
    main_naw=0
    for j in vse:
        if j != main_str:
            main_naw=j
    brauser.switch_to.window(main_naw)
    print(brauser.current_window_handle)
    brauser.close()
    brauser.switch_to.window(main_str)






