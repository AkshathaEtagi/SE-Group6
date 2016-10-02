from bs4 import BeautifulSoup
import requests
import re

url_to_scrape='http://www.medguideindia.com/show_brand.php?nav_link=&pageNum_rr=0&nav_link=&selectme=0'
first_part='http://www.medguideindia.com/show_brand.php?nav_link=&pageNum_rr='
second_part = '&nav_link=&selectme='

for i in range(0,1):
	url = first_part + str(i) +second_part + str(i)
	r=requests.get(url)
	soup=BeautifulSoup(r.text, "html.parser")
	medicine_link=[]

	records = soup.find('table',{'class':'tabsborder2'}).findAll('tr',{'class':'row'})
	for record in records:
		active_link=record.findAll('td')[-1].find('a')['onclick'][12:][:-2]
		active_linkfinal= 'http://www.medguideindia.com/' +active_link
		#print(active_linkfinal)
		medicine_link.append(active_linkfinal)
		#print(medicine_link)

		final_details=[]                                             #final details contains all active ingredients.

	for i in medicine_link[:5]:
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
#if we print final_details we will get the list of all the active ingredients

