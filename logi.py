import os
import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


brauser=webdriver.Chrome()
brauser.implicitly_wait(10)

brauser.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')

allelements=brauser.find_elements(By.CSS_SELECTOR,"table.dataTable tr")

for i in range(len(allelements)):
    all=brauser.find_elements(By.CSS_SELECTOR,"table.dataTable tr")
    element=all[i]

    for l in brauser.get_log("browser"):
       print(l)

allel=brauser.find_elements(By.XPATH, "//td[3]/a")
mass=[]
for l in allel:
    el=l.get_attribute('href')
    mass.append(el)

for k in range(len(mass)):
    brauser.get(mass[k])
    for l in brauser.get_log("browser"):
        print(l)
print(mass)

time.sleep(2)