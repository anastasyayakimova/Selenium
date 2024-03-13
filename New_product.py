import os
import pickle
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC


brauser=webdriver.Chrome()
brauser.implicitly_wait(10)

brauser.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')

add_new_prod=brauser.find_element(By.XPATH,"//div[@style='float: right;']/a[2]").click()

Name=brauser.find_element(By.CSS_SELECTOR,"input[name='name[en]']").send_keys("New Utka")
Code=brauser.find_element(By.CSS_SELECTOR,"input[name='code']").send_keys("12345678")
Gender=brauser.find_element(By.CSS_SELECTOR,"input[value='1-2']").click()

quantity=brauser.find_element(By.CSS_SELECTOR,"input[name='quantity']").click()
brauser.find_element(By.CSS_SELECTOR,"input[name='quantity']").clear()
brauser.find_element(By.CSS_SELECTOR,"input[name='quantity']").send_keys('4')

sel=brauser.find_element(By.CSS_SELECTOR,"select[name='sold_out_status_id']")
select=Select(sel)
select.select_by_visible_text('Temporary sold out')

#Даты и файл
relative_patch="utka.jpg"
absolute=os.path.abspath(relative_patch)
print(absolute)
imag=brauser.find_element(By.CSS_SELECTOR,"input[name='new_images[]']").send_keys(absolute)

datavaildfrom=brauser.find_element(By.CSS_SELECTOR,"input[name='date_valid_from']").click()
brauser.find_element(By.CSS_SELECTOR,"input[name='date_valid_from']").send_keys("13.03.2024")
datavaildto=brauser.find_element(By.CSS_SELECTOR,"input[name='date_valid_to']").click()
brauser.find_element(By.CSS_SELECTOR,"input[name='date_valid_to']").send_keys("13.04.2024")

brauser.find_element(By.LINK_TEXT,'Information').click()
manuf=brauser.find_element(By.CSS_SELECTOR,"select[name='manufacturer_id']")
manufacturer=Select(manuf)
manufacturer.select_by_visible_text("ACME Corp.")

keywords=brauser.find_element(By.CSS_SELECTOR,"input[name='keywords']").send_keys("3456722")
shortDescription=brauser.find_element(By.CSS_SELECTOR,"input[name='short_description[en]']").send_keys("UTK")
description=brauser.find_element(By.CSS_SELECTOR,"div.trumbowyg-editor").send_keys("Это новая утка")
headTitle=brauser.find_element(By.CSS_SELECTOR,"input[name='head_title[en]']").send_keys('utkf цветная')
metaDescription=brauser.find_element(By.CSS_SELECTOR,"input[name='meta_description[en]']").send_keys('test')

brauser.find_element(By.LINK_TEXT,'Prices').click()
brauser.find_element(By.CSS_SELECTOR,"input[name='purchase_price']").click()
brauser.find_element(By.CSS_SELECTOR,"input[name='purchase_price']").clear()
brauser.find_element(By.CSS_SELECTOR,"input[name='purchase_price']").send_keys("3")
purchPrice=brauser.find_element(By.CSS_SELECTOR,"select[name='purchase_price_currency_code']")
purchasePrice=Select(purchPrice)
purchasePrice.select_by_visible_text('US Dollars')

inclpriceusd=brauser.find_element(By.CSS_SELECTOR,"input[name='gross_prices[USD]']").click()
inclpriceusd=brauser.find_element(By.CSS_SELECTOR,"input[name='gross_prices[USD]']").clear()
inclpriceusd=brauser.find_element(By.CSS_SELECTOR,"input[name='gross_prices[USD]']").send_keys('3')

inclpriceeur=brauser.find_element(By.CSS_SELECTOR,"input[name='gross_prices[EUR]']").click()
inclpriceeur=brauser.find_element(By.CSS_SELECTOR,"input[name='gross_prices[EUR]']").clear()
inclpriceeur=brauser.find_element(By.CSS_SELECTOR,"input[name='gross_prices[EUR]']").send_keys('2')

Save=brauser.find_element(By.CSS_SELECTOR,"button[name='save']").click()

try:
    brauser.find_element(By.LINK_TEXT, "New Utka")
    print("True")
except NoSuchElementException:
    print("False")


time.sleep(3)