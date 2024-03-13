import time
import random
from random import choice, sample
import string
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]
def get_random_domain(domains): return random.choice(domains)
def get_random_name(letters, length): return ''.join(random.choice(letters) for i in range(length))
def generate_random_emails(nb, length): return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]
def generate_mail(): return (generate_random_emails(1, 7))

brauser=webdriver.Chrome()
brauser.implicitly_wait(10)
brauser.get('http://localhost/litecart/en/create_account')

first_name=brauser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Anastasya")
last_name=brauser.find_element(By.CSS_SELECTOR,"input[name='lastname']").send_keys("Yakim")
Address_1=brauser.find_element(By.CSS_SELECTOR,"input[name='address1']").send_keys("Voroneg, Nevskogo12a")
Postcode=brauser.find_element(By.CSS_SELECTOR,"input[name='postcode']").send_keys("98766")
City=brauser.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Voroneg")

sel=brauser.find_element(By.CSS_SELECTOR,"span.select2-selection__arrow").click()
element=brauser.find_element(By.CSS_SELECTOR,"input.select2-search__field").send_keys("Algeria" + Keys.ENTER)

email=generate_mail()
Email=brauser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)

Phone=brauser.find_element(By.CSS_SELECTOR,"input[name='phone']").send_keys("876543567")
D_passord=brauser.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("12345678")
C_password=brauser.find_element(By.CSS_SELECTOR,"input[name='confirmed_password']").send_keys("12345678")
create_account=brauser.find_element(By.CSS_SELECTOR,"button[name='create_account']").click()

logout=brauser.find_element(By.LINK_TEXT,"Logout").click()

login_email=brauser.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys(email)
login_password=brauser.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys('12345678')
login=brauser.find_element(By.CSS_SELECTOR,"button[name='login']").click()
brauser.find_element(By.LINK_TEXT,"Logout").click()


time.sleep(2)
