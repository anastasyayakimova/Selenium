import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

brauser=webdriver.Chrome()
brauser.implicitly_wait(10)
brauser.get('http://localhost/litecart/en/')

compaings=brauser.find_elements(By.CSS_SELECTOR, "div#box-campaigns li")
prise_regular_color1='rgba(119, 119, 119, 1)'
prise_compain_color1='rgba(204, 0, 0, 1)'
line_through='line-through solid rgb(119, 119, 119)'
text=0
prise_regular=0
prise_campaign=0
prise_regular_height=0
prise_campaign_height=0
prise_regular_color=0
prise_campaign_color=0
prise_regular_line=0
prise_campaign_weight=0

for i in compaings:
    t=i.find_element(By.CSS_SELECTOR, "div#box-campaigns li div.name")
    text=t.text
    print(text)
    p=i.find_element(By.CSS_SELECTOR, "div#box-campaigns li div.price-wrapper s")
    prise_regular=p.text
    print(prise_regular)
    ps=i.find_element(By.CSS_SELECTOR, "div#box-campaigns li div.price-wrapper strong")
    prise_campaign=ps.text
    print(prise_campaign)
    prise_regular_height=p.get_attribute('offsetHeight')
    print(prise_regular_height)
    prise_campaign_height=ps.get_attribute('offsetHeight')
    print(prise_campaign_height)
    assert prise_campaign_height>prise_regular_height

    prise_regular_color=p.value_of_css_property('color')
    print(prise_regular_color)
    assert prise_regular_color==prise_regular_color1
    prise_regular_line=p.value_of_css_property('text-decoration')
    print(prise_regular_line)
    assert prise_regular_line==line_through

    prise_campaign_color=ps.value_of_css_property('color')
    print(prise_campaign_color)
    assert  prise_campaign_color==prise_compain_color1
    prise_campaign_weight=ps.value_of_css_property('font-weight')
    print(prise_campaign_weight)

links=brauser.find_elements(By.CSS_SELECTOR, "div#box-campaigns a.link")
link=[]
for j in links:
    l=j.get_attribute('href')
    link.append(l)
print(link)

h1=0
prise_regular2=0
prise_campaign2=0
prise_regular2_height=0
prise_campaign2_height=0
prise_regular2_color=0
prise_campaign2_color=0
prise_regular2_color1='rgba(102, 102, 102, 1)'
prise_campaign2_color1='rgba(204, 0, 0, 1)'
prise_regular_line=0
text_dec='line-through solid rgb(102, 102, 102)'
bold_compaign=0
for l in range(len(link)):
    brauser.get(link[l])
    h1=brauser.find_element(By.CSS_SELECTOR, "h1").text
    assert h1==text

    pg2=brauser.find_element(By.CSS_SELECTOR, "div.price-wrapper s")
    prise_regular2=pg2.text
    print(prise_regular2)
    assert prise_regular2==prise_regular
    prise_regular2_height=pg2.get_attribute("offsetHeight")
    prise_regular2_color=pg2.value_of_css_property("color")
    print(prise_regular2_color)
    assert prise_regular2_color1==prise_regular2_color
    prise_regular_line=pg2.value_of_css_property('text-decoration')
    print(prise_regular_line)
    assert prise_regular_line==text_dec

    pc2=brauser.find_element(By.CSS_SELECTOR,"div.price-wrapper strong")
    prise_campaign2=pc2.text
    print(prise_campaign2)
    assert prise_campaign2==prise_campaign
    prise_campaign2_height=pc2.get_attribute("offsetHeight")
    assert prise_campaign2_height>prise_regular2_height
    prise_campaign2_color=pc2.value_of_css_property("color")
    print(prise_campaign2_color)
    assert prise_campaign2_color1==prise_campaign2_color
    bold_compaign=pc2.value_of_css_property("font-weight")
    print(bold_compaign)











