import pickle
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def find_element_h(brauser, element):
    try:
        brauser.find_element(By.CSS_SELECTOR, 'h1')
        return True
    except NoSuchElementException:
        return False


brauser = webdriver.Chrome()
brauser.implicitly_wait(10)

brauser.get('http://localhost/litecart/admin/')
for cookie in pickle.load(open('test', 'rb')):
    brauser.add_cookie(cookie)

brauser.get('http://localhost/litecart/admin/')

index_1 = brauser.find_element(By.CSS_SELECTOR, "ul#box-apps-menu li")
index_1.click()
time.sleep(2)

index_11 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-template').click()
element_11 = brauser.get('http://localhost/litecart/admin/?app=appearance&doc=template')
h11 = find_element_h(brauser, element_11)
print(h11)

index_12 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-logotype').click()
element_12 = brauser.get('http://localhost/litecart/admin/?app=appearance&doc=logotype')
h12 = find_element_h(brauser, element_12)
print(h12)

index_2 = brauser.find_element(By.XPATH, "//span[text()='Catalog']/../parent::li").click()
index_21 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-catalog')
element_21 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')
h21 = find_element_h(brauser, element_21)
print(h21)

index_22 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-product_groups')
element_22 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=product_groups')
h22 = find_element_h(brauser, element_22)
print(h22)

index_23 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-option_groups')
element_23 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=product_groups')
h23 = find_element_h(brauser, element_23)
print(h23)

index_23 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-option_groups')
element_23 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=option_groups')
h23 = find_element_h(brauser, element_23)
print(h23)

index_24 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-manufacturers')
element_24 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=manufacturers')
h24 = find_element_h(brauser, element_24)
print(h24)

index_25 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-suppliers')
element_25 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=suppliers')
h25 = find_element_h(brauser, element_25)
print(h25)

index_26 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-delivery_statuses')
element_26 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=delivery_statuses')
h26 = find_element_h(brauser, element_26)
print(h26)

index_27 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-sold_out_statuses')
element_27 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=sold_out_statuses')
h27 = find_element_h(brauser, element_27)
print(h27)

index_28 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-quantity_units')
element_28 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=quantity_units')
h28 = find_element_h(brauser, element_28)
print(h28)

index_29 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-csv')
element_29 = brauser.get('http://localhost/litecart/admin/?app=catalog&doc=csv')
h29 = find_element_h(brauser, element_29)
print(h29)

index_3 = brauser.find_element(By.XPATH, "//span[text()='Countries']/../parent::li").click()
element_3 = brauser.get('http://localhost/litecart/admin/?app=countries&doc=countries')
h3 = find_element_h(brauser, element_3)
print(h3)

index_4 = brauser.find_element(By.XPATH, "//span[text()='Currencies']/../parent::li").click()
element_4 = brauser.get('http://localhost/litecart/admin/?app=currencies&doc=currencies')
h4 = find_element_h(brauser, element_4)
print(h4)

index_5 = brauser.find_element(By.XPATH, "//span[text()='Customers']/../parent::li").click()
element_51 = brauser.get('http://localhost/litecart/admin/?app=customers&doc=customers')
h51 = find_element_h(brauser, element_51)
print(h51)

index_52 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-csv')
element_52 = brauser.get('http://localhost/litecart/admin/?app=customers&doc=csv')
h52 = find_element_h(brauser, element_52)
print(h52)

index_53 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-newsletter')
element_53 = brauser.get('http://localhost/litecart/admin/?app=customers&doc=newsletter')
h53 = find_element_h(brauser, element_53)
print(h53)

index_6 = brauser.find_element(By.XPATH, "//span[text()='Geo Zones']/../parent::li").click()
element_6 = brauser.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
h6 = find_element_h(brauser, element_6)
print(h6)

index_7 = brauser.find_element(By.XPATH, "//span[text()='Languages']/../parent::li").click()
index_71 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-languages')
element_71 = brauser.get('http://localhost/litecart/admin/?app=languages&doc=languages')
h71 = find_element_h(brauser, element_71)
print(h71)

index_72 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-storage_encoding')
element_72 = brauser.get('http://localhost/litecart/admin/?app=languages&doc=storage_encoding')
h72 = find_element_h(brauser, element_72)
print(h72)

index_8 = brauser.find_element(By.XPATH, "//span[text()='Modules']/../parent::li").click()
index_81 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-jobs')
element_81 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=jobs')
h81 = find_element_h(brauser, element_81)
print(h81)

index_82 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-customer')
element_82 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=customer')
h82 = find_element_h(brauser, element_82)
print(h82)

index_83 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-shipping')
element_83 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=shipping')
h83 = find_element_h(brauser, element_83)
print(h83)

index_84 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-payment')
element_84 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=payment')
h84 = find_element_h(brauser, element_84)
print(h84)

index_85 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-order_total')
element_85 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=order_total')
h85 = find_element_h(brauser, element_85)
print(h85)

index_86 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-order_success')
element_86 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=order_success')
h86 = find_element_h(brauser, element_86)
print(h86)

index_87 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-order_action')
element_87 = brauser.get('http://localhost/litecart/admin/?app=modules&doc=order_action')
h87 = find_element_h(brauser, element_87)
print(h87)

index_9 = brauser.find_element(By.XPATH, "//span[text()='Orders']/../parent::li").click()
index_91 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-orders')
brauser.get('http://localhost/litecart/admin/?app=orders&doc=orders')
h91 = find_element_h(brauser, element_91)
print(h91)

index_92 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-order_statuses')
brauser.get('http://localhost/litecart/admin/?app=orders&doc=order_statuses')
h92 = find_element_h(brauser, element_92)
print(h92)

brauser.find_element(By.XPATH, "//span[text()='Pages']/../parent::li").click()
element_10 = brauser.get('http://localhost/litecart/admin/?app=pages&doc=pages')
h10 = find_element_h(brauser, element_10)
print(h10)

index_11 = brauser.find_element(By.XPATH, "//span[text()='Reports']/../parent::li").click()
element_11 = brauser.get('http://localhost/litecart/admin/?app=pages&doc=pages')
h11 = find_element_h(brauser, element_11)
print(h11)

index_12 = brauser.find_element(By.XPATH, "//span[text()='Settings']/../parent::li").click()
index_121 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-store_info')
element_121 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=store_info')
h121 = find_element_h(brauser, element_121)
print(h121)

index_122 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-defaults')
element_122 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=defaults')
h122 = find_element_h(brauser, element_122)
print(h122)

index_123 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-general')
element_123 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=general')
h123 = find_element_h(brauser, element_123)
print(h123)

index_124 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-listings')
element_124 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=listings')
h124 = find_element_h(brauser, element_124)
print(h124)

index_125 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-images')
element_125 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=images')
h125 = find_element_h(brauser, element_125)
print(h125)

index_126 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-checkout')
element_126 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=checkout')
h126 = find_element_h(brauser, element_126)
print(h126)

index_127 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-advanced')
element_127 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=advanced')
h127 = find_element_h(brauser, element_127)
print(h127)

index_128 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-security')
element_128 = brauser.get('http://localhost/litecart/admin/?app=settings&doc=security')
h128 = find_element_h(brauser, element_128)
print(h128)

index_13 = brauser.find_element(By.XPATH, "//span[text()='Slides']/../parent::li").click()
element_13 = brauser.get('http://localhost/litecart/admin/?app=slides&doc=slides')
h13 = find_element_h(brauser, element_13)
print(h13)

index_14 = brauser.find_element(By.XPATH, "//span[text()='Tax']/../parent::li").click()
index_141 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-tax_classes')
element_141 = brauser.get('http://localhost/litecart/admin/?app=tax&doc=tax_classes')
h141 = find_element_h(brauser, element_141)
print(h141)

index_142 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-tax_rates')
element_142 = brauser.get('http://localhost/litecart/admin/?app=tax&doc=tax_rates')
h142 = find_element_h(brauser, element_142)
print(h142)

index_15 = brauser.find_element(By.XPATH, "//span[text()='Translations']/../parent::li").click()
index_151 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-search')
element_151 = brauser.get('http://localhost/litecart/admin/?app=translations&doc=search')
h151 = find_element_h(brauser, element_151)
print(h151)

index_152 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-scan')
element_152 = brauser.get('http://localhost/litecart/admin/?app=translations&doc=scan')
h152 = find_element_h(brauser, element_152)
print(h152)

index_153 = brauser.find_element(By.CSS_SELECTOR, 'li#doc-csv')
element_153 = brauser.get('http://localhost/litecart/admin/?app=translations&doc=csv')
h153 = find_element_h(brauser, element_153)
print(h153)

index_16 = brauser.find_element(By.XPATH, "//span[text()='Users']/../parent::li").click()
element_16 = brauser.get('http://localhost/litecart/admin/?app=users&doc=users')
h16 = find_element_h(brauser, element_16)
print(h16)

index_17 = brauser.find_element(By.XPATH, "//span[text()='vQmods']/../parent::li").click()
element_17 = brauser.get('http://localhost/litecart/admin/?app=vqmods&doc=vqmods')
h17 = find_element_h(brauser, element_17)
print(h17)
