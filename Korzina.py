import time
import telnetlib
import string,random
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

brauser=webdriver.Chrome()
brauser.implicitly_wait(10)
brauser.get('http://localhost/litecart/en/')

for i in range(1,4):
    elements=brauser.find_elements(By.CSS_SELECTOR,"li.product")
    random_index=random.randint(1, len(elements)-1)
    element=elements[random_index].find_element(By.CSS_SELECTOR, "a.link").click()
    try:
        sel=brauser.find_element(By.CSS_SELECTOR,"select[name='options[Size]']")
        select=Select(sel)
        select.select_by_visible_text('Small')
        brauser.find_element(By.CSS_SELECTOR, "button[name='add_cart_product']").click()
        wait=WebDriverWait(brauser,10)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH,".//*[ @ id = 'cart']//a//span[@class='quantity']"),str(i)))
        brauser.get('http://localhost/litecart/en/')
    except NoSuchElementException:
        button=brauser.find_element(By.CSS_SELECTOR, "button[name='add_cart_product']").click()

        wait=WebDriverWait(brauser,10)
        element = wait.until(EC.text_to_be_present_in_element((By.XPATH,".//*[ @ id = 'cart']//a//span[@class='quantity']"),str(i)))
        brauser.get('http://localhost/litecart/en/')


brauser.get("http://localhost/litecart/en/checkout")
quk=brauser.find_elements(By.CSS_SELECTOR,"td.sku")
for j in range(len(quk)):
    delit=brauser.find_element(By.NAME,"remove_cart_item").click()
    wait=WebDriverWait(brauser,10)
    wait.until(EC.staleness_of(quk[0]))
time.sleep(2)