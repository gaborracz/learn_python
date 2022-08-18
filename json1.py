import json

data = """
[
    {
        "id" : "1001",
        "x" : "2",
        "name" : "Gabor"
    },
    {
        "id" : "9000",
        "x" : "7",
        "name" : "Guest"
    }
]
"""

info = json.loads(data)

print("User count:", len(info))

for item in info : 
    print("ID:", item['id'])
    print("Name:", item['name'])
    print("Attribute:", item['x'])
