import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

brauser=webdriver.Chrome()
brauser.implicitly_wait(10)

def find_element_h(brauser, element):
    try:
        brauser.find_elements(By.CSS_SELECTOR, 'h1')
        return True
    except NoSuchElementException:
        return False

brauser.get('http://localhost/litecart/admin/')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/')

brauser.implicitly_wait(5)
elements=brauser.find_elements(By.XPATH, '//*[@id="app-"]/a/span[2]')
print(elements)

for i in range(len(elements)):
    elements_el=brauser.find_elements(By.XPATH, "//*[@id='app-']/a/span[2]")
    link_name=elements_el[i].text
    print(str(i)+"."+link_name)
    elements_el[i].click()

    brauser.implicitly_wait(2)
    pod_menu=brauser.find_elements(By.XPATH, "//ul[@class='docs']//li//span")
    print ("Количество вложенных элементов:"+str(len(pod_menu)))

    if len(pod_menu)<1:
        title=brauser.find_element(By.XPATH, "//td[@id='content']//h1").text
        print(link_name)
        print(title)

    for j in range(len(pod_menu)):
        pod_menu_el=brauser.find_elements(By.XPATH, "//ul[@class='docs']//li//span")
        pod_menu_el[j].click()
        pod_menu_el=brauser.find_elements(By.XPATH, "//ul[@class='docs']//li//span")
        pod_menu_name=pod_menu_el[j].text
        title2=brauser.find_element(By.XPATH, "//td[@id='content']//h1").text
        print(pod_menu_name)
        print(title2)


