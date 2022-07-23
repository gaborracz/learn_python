# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
# read the XML data from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
my_context = ssl.create_default_context()
my_context.check_hostname = False
my_context.verify_mode = ssl.CERT_NONE

url = input("Please enter a URL: ")

print("Retrieving URL:", url)

xml = urllib.request.urlopen(url, context=my_context).read()

print("Retrieved %d characters." % len(xml))

tree = ET.fromstring(xml)

lst = tree.findall('comments/comment')

numbers = list()

for element in lst :
    numbers.append(int(element.find('count').text))

print("Count:", len(numbers))

print("Sum:", sum(numbers))