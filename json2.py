import json

data = """
    {
        "name" : "Gabor",
        "phone" : {
            "type" : "intl",
            "number" : "+36 30 123 4567"
        },
        "email" : {
            "hide" : "yes"
        }
    }
"""

info = json.loads(data)

print("Name:", info["name"])
print("Phone:", info["phone"]["number"])