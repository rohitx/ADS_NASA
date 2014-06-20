import json
import urllib2

response = urllib2.urlopen("http://labs.adsabs.harvard.edu/adsabs/api/record/2014PhRvD..89b3507B?dev_key=Qmu7WDIQTcLG3RRX")
data = json.load(response)
keywords = data["keyword"]
journal  = data["pub"]
pubdate = data["pubdate"]

def clean_unicode(a_list):
	clean_list = []
	for element in a_list:
		this_element = element.encode('ascii', 'ignore')
		clean_list.append(this_element)
	return clean_list



#keyword_list =[]
#for keyword in keywords:
#	this_keyword = keyword.encode('ascii', 'ignore')
#	keyword_list.append(this_keyword)

keyword_list = clean_unicode(keywords)

print journal
print pubdate
print keyword_list