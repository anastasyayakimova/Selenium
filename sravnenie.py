import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

brauser=webdriver.Chrome()
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
    font_sizeP=p.value_of_css_property('font-size')
    fsp=font_sizeP.replace('px',"")
    print(fsp)
    font_sizePS=ps.value_of_css_property("font-size")
    fsps=font_sizePS.replace('px',"")
    print(fsps)
    assert float(fsp)<float(fsps)

    #цвет
    prise_regular_color=p.value_of_css_property('color')
    prc=Color.from_string(prise_regular_color).rgba
    print(prc)

    ppp=prc.replace('rgba(',"").replace(")","")
    prc=ppp.split(', ')
    assert prc[0]==prc[1]==prc[2]

    prise_campaign_color=ps.value_of_css_property('color')
    pcc=Color.from_string(prise_campaign_color).rgba
    print(pcc)

    ccc=pcc.replace('rgba(',"").replace(")","")
    pcc=ccc.split(', ')
    assert pcc[1]=='0'
    assert pcc[2]=='0'

    prise_campaign_weight=ps.value_of_css_property('font-weight')
    print(prise_campaign_weight)
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
    prise_regular2_size=pg2.value_of_css_property("font-size")
    pr2s=prise_regular2_size.replace('px',"")
    print(pr2s)

    pc2=brauser.find_element(By.CSS_SELECTOR,"div.price-wrapper strong")
    prise_campaign2_size=pc2.value_of_css_property('font-size')
    pc2s=prise_campaign2_size.replace('px',"")
    print(pc2s)
    assert float(pr2s)<float(pc2s)

    prise_campaign2=pc2.text
    print(prise_campaign2)
    assert prise_campaign2==prise_campaign
    #цвет
    prise_regular2_color=pg2.value_of_css_property("color")
    pr2cc=Color.from_string(prise_regular2_color).rgba
    print(pr2cc)
    pr2c=pr2cc.replace('rgba(',"").replace(")","")
    prc2=pr2c.split(', ')
    assert prc2[0]==prc2[1]==prc2[2]

    prise_campaign2_color=pc2.value_of_css_property("color")
    pc2cc=Color.from_string(prise_campaign2_color).rgba
    print(pc2cc)
    pc2c=pc2cc.replace('rgba(',"").replace(")","")
    pcc2=pc2c.split(', ')
    assert pcc2[1]=='0'
    assert pcc2[2]=='0'

    bold_compaign=pc2.value_of_css_property("font-weight")
    print(bold_compaign)

    prise_regular_line=pg2.value_of_css_property('text-decoration-line')
    print(prise_regular_line)
    assert prise_regular_line==text_dec











