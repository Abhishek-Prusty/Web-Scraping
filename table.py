import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pickle

driver = webdriver.Firefox()
driver.get("http://bhoomi.csa.iisc.ernet.in:8080/ihg/manuscript_editor/tableprocessing_mand.jsp")

table=driver.find_element_by_xpath('/html/body/form/div/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[3]/td[3]/div/table/tbody[3]')
rows=table.find_elements_by_tag_name("tr")

store={}
l=0
for row in rows:
	name=""
	temp=row.find_elements_by_tag_name("td")
	#print(len(temp))
	name=temp[0].text+temp[1].text+temp[2].text
	key=temp[3].text
	store[name]=key

print(store)

f=open('dictionary.pkl',"wb")
pickle.dump(store,f)
f.close()

