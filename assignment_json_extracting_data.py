import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Please enter a URL: ")

print("Retrieving", url)

html = urllib.request.urlopen(url, context=ctx)

data = html.read().decode()

print("Retrieved: %d bytes." % len(data))

json_data = json.loads(data)

# print(json.dumps(json_data, indent=3))

numbers = list()

for item in json_data["comments"] :
    numbers.append(item["count"])

print("Count:", len(numbers))
print("Sum:", sum(numbers))