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



language = pickle.load( open( "dictionary.pkl", "rb" ) )
driver = webdriver.Firefox()
driver.get("http://bhoomi.csa.iisc.ernet.in:8080/ihg/manuscript_editor/processing.jsp")
driver.maximize_window()

#page=requests.get("http://bhoomi.csa.iisc.ernet.in:8080/ihg/manuscript_editor/processing.jsp")
#soup=BeautifulSoup(page.content,'html.parser')

flag=0
element = driver.find_element_by_xpath('//*[@id="dropdownlist1"]')
all_options = element.find_elements_by_tag_name("option")
ln=len(all_options)
for i in range(ln):
	if(i==0):
		continue
	print("Manuscript name: %s" % all_options[i].get_attribute("value"))
	man=all_options[i].get_attribute("value")
	all_options[i].click()


	element2 = driver.find_element_by_xpath('//*[@id="dropdownlist2"]')
	all_options2 = element2.find_elements_by_tag_name("option")
	ln2=len(all_options2)
	for j in range(ln2):
		if(j==0):
			continue
		print("Lib abbr: %s" % all_options2[j].get_attribute("value"))
		abbr=all_options2[j].get_attribute("value")
		all_options2[j].click()
		element2 = driver.find_element_by_xpath('//*[@id="dropdownlist2"]')
		all_options2 = element2.find_elements_by_tag_name("option")

		element3=driver.find_element_by_xpath('//*[@id="dropdownlist3"]')
		all_options3=element3.find_elements_by_tag_name("option")
		ln3=len(all_options3)
		for k in range(ln3):
			if(k==0):
				continue
			print("Manuscript version: %s" % all_options3[k].get_attribute("value"))
			ver=all_options3[k].get_attribute("value")
			all_options3[k].click()
			element3 = driver.find_element_by_xpath('//*[@id="dropdownlist3"]')
			all_options3 = element3.find_elements_by_tag_name("option")

			prev_no=0
			l=1
			element4=driver.find_element_by_xpath('/html/body/form/div/table/tbody[1]/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[6]/td/div/table/tbody/tr[2]/td[2]/div/div[2]/input')
			element4.click()
			element4.send_keys(Keys.BACK_SPACE)
			element4.send_keys(Keys.BACK_SPACE)
			element4.send_keys(Keys.BACK_SPACE)
			element4.send_keys(1)
			#time.sleep(0.1)


			for l in range(2,100):
				'''
				element4=driver.find_element_by_xpath('/html/body/form/div/table/tbody[1]/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[6]/td/div/table/tbody/tr[2]/td[2]/div/div[2]/div[5]')
				WebDriverWait(driver, 10).until_not(EC.visibility_of_element_located((By.ID, "overley")))
				element4.click()
				time.sleep(1)
				'''
				btn=driver.find_element_by_xpath('/html/body/form/div/table/tbody[1]/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[6]/td/div/table/tbody/tr[2]/td[3]/span/input')
				btn.click()

				image=driver.find_element_by_id("myimage").get_attribute("src")
				#print("yoooooo")
				metadata=driver.find_element_by_xpath('//*[@id="html_file"]')

				print("leaf_number: {} , ".format(l-1),image)
				print("language: {} ,".format(language[man+abbr+ver]) )
				print("metadata",metadata.get_attribute("value"))


				leaf_number=driver.find_element_by_xpath('/html/body/form/div/table/tbody[1]/tr[2]/td/table/tbody/tr[3]/td[3]/table/tbody/tr[3]/td[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[6]/td/div/table/tbody/tr[2]/td[2]/div/div[2]/input')
				leaf_number.click()
				leaf_number.send_keys(Keys.BACK_SPACE)
				leaf_number.send_keys(Keys.BACK_SPACE)
				leaf_number.send_keys(Keys.BACK_SPACE)
				#time.sleep(0.1)
				leaf_number.send_keys(l)
				leaf_number.send_keys(Keys.ENTER)
				
				#time.sleep(0.1)

				no=leaf_number.get_attribute("value")

				if(no==prev_no):
					break
				prev_no=no


		element2 = driver.find_element_by_xpath('//*[@id="dropdownlist2"]')
		all_options2 = element2.find_elements_by_tag_name("option")


	element = driver.find_element_by_xpath('//*[@id="dropdownlist1"]')
	all_options = element.find_elements_by_tag_name("option")
	flag=1







