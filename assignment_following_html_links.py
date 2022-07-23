# In this assignment you will write a Python program that expands on 
# http://www.py4e.com/code3/urllinks.py. The program will use urllib 
# to read the HTML from the data files below, extract the href= vaues 
# from the anchor tags, scan for a tag that is in a particular position 
# relative to the first name in the list, follow that link and repeat the 
# process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
my_context = ssl.create_default_context()
my_context.check_hostname = False
my_context.verify_mode = ssl.CERT_NONE

url = input("Please enter a URL: ")

count = int(input("Enter count: "))

position = int(input("Enter position: "))


for i in range(count + 1) :

    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=my_context).read()
    my_soup = BeautifulSoup(html, 'html.parser')
    tags = my_soup('a')
    links = list()

    for tag in tags :

        x = tag.contents[0]
        y = tag.get("href", None)
        links.append(y)
        
    url = links[position - 1]

    links = links.clear()