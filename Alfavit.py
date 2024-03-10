import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

brauser=webdriver.Chrome()
brauser.implicitly_wait(10)

brauser.get('http://localhost/litecart/admin/?app=countries&doc=countries')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/?app=countries&doc=countries')
time.sleep(5)

countries=brauser.find_elements(By.XPATH, ".//table[@class='dataTable']//tr[@class='row']")
masscountries=[]
masszone=[]
index_fo_link=[]
count=0
for i in countries:
    column=i.find_elements(By.TAG_NAME, "td")
    masscountries.append(column[4].text)
    if int(column[5].text)>0:
        index_fo_link.append(i)
    count+=1
sorted_mass_contries=sorted(masscountries)
assert masscountries == sorted_mass_contries

print(index_fo_link)
sort_zone=[]
for j in index_fo_link:
    link=j.find_element(By.CSS_SELECTOR, "td a").get_attribute('href')
    sort_zone.append(link)
print(sort_zone)

for link in range(len(sort_zone)):
    brauser.get(sort_zone[link])
    el=brauser.find_elements(By.XPATH, "//input[contains(@name, 'zones[') and contains(@name, '[name]')]/..")
    print(len(el))
    print(el)
    mass=[]
    mass_sort=[]
    for i in el:
        mass.append(i.text)
    print(mass)
    mass_sort=sorted(mass)
    print(mass_sort)
    assert mass == mass_sort






