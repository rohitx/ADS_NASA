# This program reads the JSON document and queries it for a list of authors 
#
# DEPENDENCIES: Requires a 'ads_nasa.txt' in JSON format to read in 
#               Requires PANDAS and NUMPY packages 
# 
# Written by Rohit Deshpande, 2014-02-19
#
#-------------------------------------------------
# IMPORT STATEMENTS 
#-------------------------------------------------
import json
import urllib2
import numpy as np
import pandas as pd
#-------------------------------------------------
# DEFINING FUNCTIONS 
#-------------------------------------------------

def search_list(alist, aname):
	count = 0
	author_index = 0
	author_list = alist 
	author_name = aname
	for author in author_list:
		if author == author_name:
			author_index = author_list.index(author)+1
			count = 1
	return count, author_index
#-------------------------------------------------
# READING IN FILE CONTAINING THE URLS 
#-------------------------------------------------
journal_data = np.genfromtxt('complete_ref_cleaned.txt', dtype=None, names="star, journal", usecols=(0,2), delimiter=',', skiprows=1, comments='#')
journals = journal_data['journal']


cehw_list = ["Ford, Eric B.", "Wright, Jason T.", "Kasting, James F.", "Luhman, Kevin L.", "Sigurdsson, S", "Wolszczan, A.", "Gilliland, Ronald L."]

author1_count = []

author2_count = []

author3_count = []

author4_count = []

author5_count = []

author6_count = []

author7_count = []

url_link = []
pub_year = []
pub_paper = []
run_count = 0
# Get the URL string correspond to the journal:
for element in journals:
	run_count += 1
	#print "Checking journal... ", run_count
	url_string = (element.split('/'))[-1]
	# Remove any white Spaces
	url_string = url_string.strip()
	#print url_string
	url_link.append(url_string)
	response = urllib2.urlopen('http://labs.adsabs.harvard.edu/adsabs/api/record/'+url_string+'?dev_key=Qmu7WDIQTcLG3RRX')
	data = json.load(response)
	# Get the list of Authors 
	authors = data["author"]
	# Get the Year
	publication_date = data["pubdate"]
	pub_year.append(publication_date)
	# Get the Journal 
	this_pub  = data["pub"]
	pub_paper.append(this_pub)
	# Get Keyword
	#keywords = data["keyword"]
	# Remove Unicode from Author list 
	author_list = []
	for author in authors:
		this_author = author.encode('ascii', 'ignore')
		author_list.append(this_author)
	# Find if the author is in the authorlist
	for cehw in cehw_list:
		if cehw == cehw_list[0]:
			count0, position0 = search_list(author_list, cehw)
			author1_count.append(count0)

		elif cehw == cehw_list[1]:
			count1, position1 = search_list(author_list, cehw)
			author2_count.append(count1)

		elif cehw == cehw_list[2]:
			count2, position2 = search_list(author_list, cehw)
			author3_count.append(count2)

		elif cehw == cehw_list[3]:
			count3, position3 = search_list(author_list, cehw)
			author4_count.append(count3)

		elif cehw == cehw_list[4]:
			count4, position4 = search_list(author_list, cehw)
			author5_count.append(count4)

		elif cehw == cehw_list[5]:
			count5, position5 = search_list(author_list, cehw)
			author6_count.append(count5)

		elif cehw == cehw_list[6]:
			count6, position6 = search_list(author_list, cehw)
			author7_count.append(count6)
			

# Creating a dictionary with people in CEHW 
x = {}
x["URL_link"]        = url_link
x["Ford_count"]    = author1_count
x["Wright_count"]    = author2_count
x["Kasting_count"]    = author3_count
x["Luhman_count"]    = author4_count
x["Sigurdsson_count"]    = author5_count
x["Wolszczan_count"]    = author6_count
x["Gilliland_count"]    = author7_count
x["Publication_Date"] = pub_year
x["Journal"] = pub_paper

df = pd.DataFrame(x)

df.to_csv('CEHW_stats_faculty.csv')


