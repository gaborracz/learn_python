# Scraping Numbers from HTML using BeautifulSoup In this assignment 
# you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. 
# The program will use urllib to read the HTML from the data files below, 
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore ssl certificate errors
my_context = ssl.create_default_context()
my_context.check_hostname = False
my_context.verify_mode = ssl.CERT_NONE

url = input("Please enter a URL: ")

html = urlopen(url, context=my_context).read()

my_soup = BeautifulSoup(html, "html.parser")

tags = my_soup('span')

count = 0

numbers = list()

for tag in tags :
    x = tag.contents[0]
    numbers.append(int(x))
    count = count + 1

print("Count ", count)
print("Sum ", sum(numbers))