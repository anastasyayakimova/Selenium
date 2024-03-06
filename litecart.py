from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://localhost/litecart/')

def find_element_sticker(driver, element):
    try:
        sticker=driver.find_elements(By.CSS_SELECTOR, "div.sticker")
        count=len(sticker) #считает все стикеры на странице, а не в контексте данного li
        print(count)
        if count==1:
            print("1 стикер")
        else:
            print("Стикеров больше")
        return True
    except NoSuchElementException:
        return False

driver.implicitly_wait(5)
elements=driver.find_elements(By.XPATH, "//div[@id='box-most-popular']//ul/li")
for i in elements:
    print(i)
    element=driver.find_element(By.CSS_SELECTOR, 'li.hover-light')
    result=find_element_sticker(driver, element)
    print(result)

driver.implicitly_wait(5)
elementss=driver.find_elements(By.XPATH, "//div[@id='box-campaigns']//ul/li")
for i in elementss:
    print(i)
    element=driver.find_element(By.CSS_SELECTOR, 'li.hover-light')
    result=find_element_sticker(driver, element)
    print(result)

driver.implicitly_wait(5)
elementsss=driver.find_elements(By.XPATH, "//div[@id='box-latest-products']//ul/li")
for i in elementsss:
    print(i)
    element=driver.find_element(By.CSS_SELECTOR, 'li.hover-light')
    result=find_element_sticker(driver, element)
    print(result)
