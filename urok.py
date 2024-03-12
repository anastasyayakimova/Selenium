import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

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

Email=brauser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("yakiiiim@gmail.com")
Phone=brauser.find_element(By.CSS_SELECTOR,"input[name='phone']").send_keys("876543567")
D_passord=brauser.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("12345678")
C_password=brauser.find_element(By.CSS_SELECTOR,"input[name='confirmed_password']").send_keys("12345678")
create_account=brauser.find_element(By.CSS_SELECTOR,"button[name='create_account']").click()

logout=brauser.find_element(By.LINK_TEXT,"Logout").click()

login_email=brauser.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys('yakiiiim@gmail.com')
login_password=brauser.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys('12345678')
login=brauser.find_element(By.CSS_SELECTOR,"button[name='login']").click()
brauser.find_element(By.LINK_TEXT,"Logout").click()


time.sleep(2)
