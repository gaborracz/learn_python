import urllib.request, urllib.parse, urllib.error
import json

service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input("Enter a location: ")

    if len(address) < 1 : break

    url = service_url + urllib.parse.urlencode({'address' : address})

    print(url)
    
