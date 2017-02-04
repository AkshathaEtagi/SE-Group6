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

for i in range(0,1):
	url = first_part + str(i) +second_part + str(i)
	r=requests.get(url)
	soup=BeautifulSoup(r.text, "html.parser")

	table=soup.findAll(class_='row')
	for rows in table:
		cells=rows.findAll("td")
		varone=cells[0].text
		print(varone)
		sno.append(varone)
	print(sno)
	medicine_link=[]

	records = soup.find('table',{'class':'tabsborder2'}).findAll('tr',{'class':'row'})
	for record in records:
		active_link=record.findAll('td')[-1].find('a')['onclick'][12:][:-2]
		active_linkfinal= 'http://www.medguideindia.com/' +active_link
		#print(active_linkfinal)
		medicine_link.append(active_linkfinal)
		#print(medicine_link)

		final_details=[]                                             #final details contains all active ingredients.


	for i in medicine_link:
		r= requests.get(i)
		soup=BeautifulSoup(r.text,"html.parser")
		medicine_details=[]
		rank = soup.findAll("tr", {"class": "row"})
		for j in rank:
			rone=[]
			rone=j.text
			medicine_details.append(rone)
		#print(medicine_details)
		final_details.append(medicine_details)
	#print((final_details))

client=MongoClient('localhost',27017)
db=client.admin
coll=db.ingredients
record={}
snum=0


for i in final_details:
	if (snum!=50):

		print("hello")
		record={'SNo': sno[snum], 'Ingredients':i}
		snum=snum+1

		db.ingredients.insert(record)





#print("here")
#outfile= open("./output.csv", "wb")
#writer = csv.writer(outfile)
#writer.writerows(final_details)
#print("There")



	
     
	




