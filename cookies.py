import pickle
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

brauser = webdriver.Chrome()

brauser.get("http://localhost/litecart/admin/login.php")
click_button = brauser.find_element(By.NAME, "username")
click_button.click()
click_button.send_keys("admin")
click_buttonn=brauser.find_element(By.NAME, "password")
click_buttonn.click()
click_buttonn.send_keys("admin")
chek_box=brauser.find_element(By.NAME, "remember_me")
chek_box.click()
login_button=brauser.find_element(By.CSS_SELECTOR, "button[name='login']")
login_button.click()
sleep(5)
pickle.dump(brauser.get_cookies(), open('test', 'wb'))