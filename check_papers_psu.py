import ads 

# Let's create a function that will clean unicode characters 
# from a list we give it. This would be very useful for what is
# to follow 

def clean_unicode(a_list):
	clean_list = []
	for element in a_list:
		this_element = element.encode('ascii', 'ignore')
		clean_list.append(this_element)
	return clean_list



years = (2014, 2014)
months = range(1,2)

# The affiliation string to search for
my_affiliation = '"Pennsylvania State University"'

for year in xrange(years[0], years[1] + 1):
    for month in months:
        print "The year is: ", year
        print "The month is: ", month
        # Get all the articles
        articles = ads.search(
            affiliation=my_affiliation,
            filter="database:astronomy AND property:refereed",
            dates="{year}/{month}".format(year=year, month=month), rows="all")
            # ads.search yields a generator, so let's list-ify the articles for multiple use
        articles = list(articles)
        print("There were {0} articles found.".format(len(articles)))

# Let's do something interesting with the data first
# We'll sort all the articles by first-authors with our matched affiliation first.
sorted_articles = sorted(articles,
    key=lambda article: [(my_affiliation.strip('"').lower() in affiliation.lower()) for affiliation in article.aff].index(True))

# Get the bibcodes for each of the articles
sorted_article_list = [article.bibcode for article in sorted_articles]

clean_sorted_list = clean_unicode(sorted_article_list)

# Clean the list of unicode: 
print clean_sorted_list

#http://labs.adsabs.harvard.edu/adsabs/api/record/2014ApJ...781....4L/?dev_key=Qmu7WDIQTcLG3RRX
#http://labs.adsabs.harvard.edu/adsabs/api/record/2014ApJ...781....4L/metrics/?dev_key=Qmu7WDIQTcLG3RRX    

# [ads.retrieve_article(article, output_filename=article.bibcode + ".pdf") for article in sorted_articles]






