import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


brauser=webdriver.Firefox()
brauser.implicitly_wait(10)
brauser.get('http://localhost/litecart/en/')

compaings=brauser.find_elements(By.CSS_SELECTOR, "div#box-campaigns li")
line_through='line-through'
text=0
prise_regular=0
prise_campaign=0
prise_regular_height=0
prise_campaign_height=0
prise_regular_color=0
prise_campaign_color=0
prise_regular_line=0
prise_campaign_weight=0
weight=700

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
    #размер
    sizeregular=p.size
    heightwidthR=[]
    for key, value in sizeregular.items():
        heightwidthR.append(value)
    print(heightwidthR)
    sizecampaign=ps.size
    heightwidthC=[]
    for key, value in sizecampaign.items():
        heightwidthC.append(value)
    print(heightwidthC)
    assert heightwidthC[0]>heightwidthR[0]
    assert heightwidthC[1]>heightwidthR[1]
    #цвет
    prise_regular_color=p.value_of_css_property('color')
    print(prise_regular_color)
    ppp=prise_regular_color.replace('rgb(',"").replace(")","")
    prc=ppp.split(', ')
    assert prc[0]==prc[1]==prc[2]

    prise_campaign_color=ps.value_of_css_property('color')
    print(prise_campaign_color)
    ccc=prise_campaign_color.replace('rgb(',"").replace(")","")
    pcc=ccc.split(', ')
    assert pcc[1]=='0'
    assert pcc[2]=='0'

    prise_campaign_weight=ps.value_of_css_property('font-weight')
    print(prise_campaign_weight)
    assert int(prise_campaign_weight)>= weight
    #зачеркнутая линия
    prise_regular_line=p.value_of_css_property('text-decoration-line')
    print(prise_regular_line)
    assert prise_regular_line==line_through

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
prise_regular_line=0
text_dec='line-through'
bold_compaign=0
for l in range(len(link)):
    brauser.get(link[l])
    h1=brauser.find_element(By.CSS_SELECTOR, "h1").text
    assert h1==text
    pg2=brauser.find_element(By.CSS_SELECTOR, "div.price-wrapper s")
    prise_regular2=pg2.text
    print(prise_regular2)
    assert prise_regular2==prise_regular
    #размер
    prise_regular2_size=pg2.size
    pricesizeR2=[]
    for key, value in prise_regular2_size.items():
        pricesizeR2.append(value)
    print(pricesizeR2)
    pc2=brauser.find_element(By.CSS_SELECTOR,"div.price-wrapper strong")
    prise_campaign2_size=pc2.size
    pricesizeC2=[]
    for key, value in prise_campaign2_size.items():
        pricesizeC2.append(value)
    print(pricesizeC2)
    assert pricesizeR2[0]<pricesizeC2[0]
    assert pricesizeR2[1]<pricesizeC2[1]

    prise_campaign2=pc2.text
    print(prise_campaign2)
    assert prise_campaign2==prise_campaign
    #цвет
    prise_regular2_color=pg2.value_of_css_property("color")
    print(prise_regular2_color)
    pr2c=prise_regular2_color.replace('rgb(',"").replace(")","")
    prc2=pr2c.split(', ')
    assert prc2[0]==prc2[1]==prc2[2]

    prise_campaign2_color=pc2.value_of_css_property("color")
    print(prise_campaign2_color)
    pc2c=prise_campaign_color.replace('rgb(',"").replace(")","")
    pcc2=pc2c.split(', ')
    assert pcc2[1]=='0'
    assert pcc2[2]=='0'

    bold_compaign=pc2.value_of_css_property("font-weight")
    print(bold_compaign)
    assert int(bold_compaign)>=weight

    prise_regular_line=pg2.value_of_css_property('text-decoration-line')
    print(prise_regular_line)
    assert prise_regular_line==text_dec

brauser.close()











