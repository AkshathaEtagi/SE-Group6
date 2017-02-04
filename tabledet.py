from bs4 import BeautifulSoup
import requests
import re
import csv
import pymongo
from pymongo import MongoClient

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
	table=soup.findAll(class_='row')
	for rows in table:
		cells=rows.findAll("td")
		varone=cells[0].text
		print(varone)
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

client=MongoClient('localhost',27017)
db=client.admin
coll=db.details 
record={}
i=0

while(i!=50):
	print("Hello")
	record={'SNo':sno[i], 'Manufacturer': manuf[i], 'Name': name[i], 'Type Of Medicine': typeof[i], 'Category': category[i]
	,'Size Per Unit': sizeunit[i], 'Size Per Package': sizepackage[i], 'Price Per Unit': priceperunit[i], 'Total Price': totalprice[i]}
	db.details.insert(record)
	i= i+1




# print("All the data in ready to be moved from List to CSV format.")

# with open('Sno.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(sno)
# print("Sno")

# with open('manuf.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(manuf)
# print("Manuf")
# with open('name.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(name)
# print("Name")
# #with open('typeof.csv', 'w') as csvfile:
#     #writer = csv.writer(csvfile, delimiter=",")
#     #writer.writerow(typeof)

# with open('category.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(category)
# print("category")
# with open('sizeunit.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(sizeunit)
# print("sizeunit")
# with open('sizepackage.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(sizepackage)
# print("sizepackage")
# with open('totalprice.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(totalprice)
# print("totalprice")
# with open('priceperunit.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(priceperunit)
# print("priceperunit")