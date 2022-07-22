"""
    What is web scraping?
        - when a program or a script pretends to be a browser and
        retrieves web pages, looks at those web pages, extracts 
        information and then looks at more web pages.

        - search engines scrape web pages - we call this "spidering the 
        web" or "web crawling"
    
    You could do string searches the hard way or you could use the free
    software library called BeautifulSoup from www.crummy.com
    http://www.crummy.com/software/BeautifulSoup/
"""

from bs4 import BeautifulSoup

import urllib.request, urllib.parse, urllib.error

url = input('Enter a URL - ')

html = urllib.request.urlopen(url).read()

my_soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags:

tags = my_soup('a')

for tag in tags :
    print(tag.get('href', None))