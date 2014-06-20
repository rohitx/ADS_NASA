import json
import urllib2
import numpy as np
import ads 
from time import localtime

#response = urllib2.urlopen('http://labs.adsabs.harvard.edu/adsabs/api/record/'+url_string+'?dev_key=Qmu7WDIQTcLG3RRX')
my_affiliation = '"Pennsylvania State University"'

current_time = localtime()

# Just grab the last month (there are more Pythonic ways to do this)
year = current_time.tm_year - 1 if current_time.tm_mon == 1 else current_time.tm_year
month = current_time.tm_mon - 1 if current_time.tm_mon > 1 else 12

articles = ads.search(
	affiliation=my_affiliation,
    filter="database:astronomy AND property:refereed",
    dates="{year}/{month}".format(year=year, month=month))

sorted_articles = sorted(articles,
        key=lambda article: [(my_affiliation.lower() in affiliation.lower()) for affiliation in article.aff])

articles = list(articles)
print("There were {0} articles found. Sorting and downloading..".format(len(articles)))

#this_article = ads.retrieve_article(sorted_articles[0], output_filename='this_article.txt')

#[ads.retrieve_article(article, output_filename="{bibcode}.pdf".format(bibcode=article.bibcode)) for article in sorted_articles]

#print articles