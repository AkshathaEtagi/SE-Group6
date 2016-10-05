from bs4 import BeautifulSoup
import requests
import re

url_to_scrape='http://www.medguideindia.com/show_brand.php?nav_link=&pageNum_rr=0&nav_link=&selectme=0'
first_part='http://www.medguideindia.com/show_brand.php?nav_link=&pageNum_rr='
second_part = '&nav_link=&selectme='

sno=[]
manuf=[]
name=[]
typeof=[]
category=[]
sizeunit=[]
sizepackage=[]
totalprice=[]
priceperunit=[]
for i in range(0,1):
	url = first_part + str(i) +second_part + str(i)
	r=requests.get(url)
	soup=BeautifulSoup(r.text, "html.parser")
	main_details={} 
	main=[] 
	print("Hello no 1")
	table=soup.findAll(class_='row')
	#print(table)
	#count=0
	for rows in table:
		cells=rows.findAll("td")
		varone=cells[0].text
		vartwo=cells[1].text
		varthree=cells[2].text
		varfour=cells[3].text
		varfive=cells[4].text
		varsix=cells[5].text
		varseven=cells[6].text
		vareight=cells[7].text
		varnine=cells[8].text


		sno.append(varone)
		manuf.append(vartwo)
		name.append(varthree)
		typeof.append(varfour)
		category.append(varfive)
		sizeunit.append(varsix)
		sizepackage.append(varseven)
		totalprice.append(vareight)
		priceperunit.append(varnine)
	#print(sno)
	#print(manuf)
	#print(name)
	#print(typeof)
	#print(category)

	
