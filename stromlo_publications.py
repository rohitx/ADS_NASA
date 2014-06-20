# coding: utf-8

""" Retrieve all the publications with authors or co-authors from a particular institute
    in a given month. 

    In this example we will find all the publications authored (at least in part) by
    researchers at the Australian National University, Canberra."""

__author__ = "Andy Casey <acasey@mso.anu.edu.au>"

# Standard library
from time import localtime

# Module specific
import ads

if __name__ == "__main__":

    # Let's do it for *last* month
    current_time = localtime()

    # Just grab the last month (there are more Pythonic ways to do this)
    #year = current_time.tm_year - 1 if current_time.tm_mon == 1 else current_time.tm_year
    #month = current_time.tm_mon - 1 if current_time.tm_mon > 1 else 12

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

    #for i in range(len(sorted_articles)):
    #    print sorted_articles[i]


    # Great! Now let's actually do something real with these articles
    # At Mount Stromlo Observatory (the Research School of Astronomy & Astrophysics within
    # the Australian National University), we have a "monthly papers" board that shows the
    # first page of every paper published by someone at Stromlo within the last month.

    # Let's download each paper for our papers board and save them by their bibliography code.
    #[ads.retrieve_article(article, output_filename=article.bibcode + ".pdf") for article in sorted_articles]
