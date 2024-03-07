from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://localhost/litecart/')
driver.implicitly_wait(5)

elements=driver.find_elements(By.XPATH, "//ul[@class='listing-wrapper products']//li")
print(str(len(elements)))
for i in range(len(elements)):
    element=driver.find_elements(By.XPATH, "//ul[@class='listing-wrapper products']//li")
    elementi=elements[i]
    print(elementi)
    stikers=driver.find_elements(By.XPATH, "//div[starts-with(@class,'sticker')]")
    stik=stikers[i].text
    print(stik)