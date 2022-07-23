import xml.etree.ElementTree as ET

data = """
<person>
    <name>Gabor</name>
    <phone type="intl">
        +36 30 123 4444
    </phone>
    <email hide="yes"/>
</person>
"""

tree = ET.fromstring(data)

print("Name:", tree.find('name').text)

print('Attribute:', tree.find('email').get('hide'))

####################################################

input = """
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Gabor</name>
            </user>
            <user x="7">
                <id>1000</id>
                <name>Guest</name>
            </user>
        </users>
    </stuff>
"""

stuff = ET.fromstring(input)

list = stuff.findall('users/user')

print("User count:", len(list))

for i in list :
    print("Name:", i.find('name').text)
    print("Id:", i.find("id").text)
    print("Attribute:", i.get("x"))