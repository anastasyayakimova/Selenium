import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

brauser=webdriver.Chrome()
brauser.implicitly_wait(10)

brauser.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')

elements=brauser.find_elements(By.XPATH, "//tr[@class='row']")
link=[]
for i in elements:
    links=i.find_element(By.CSS_SELECTOR, "tr.row td a").get_attribute('href')
    print(links)
    link.append(links)
print(link)

for l in range(len(link)):
    brauser.get(link[l])
    time.sleep(3)
    elements=brauser.find_elements(By.XPATH, "//select[contains(@name, 'zones[') and contains(@name, '][zone_code]')]/option[@selected='selected']")
    print(elements)
    print(len(elements))
    mass=[]
    mass_sort=[]
    for i in elements:
        mass.append(i.text)
    mass_sort=sorted(mass)
    assert mass==mass_sort
