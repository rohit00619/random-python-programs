import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>chuck</name>
        </user>
        <user x= "7">
            <id>002</id>
            <name>Brent</name>
            </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst= stuff.findall('users/user')
print('User Count:', len(lst))
for item in lst:
    print('Id:', item.find('id').text)
    print('Name:', item.find('name').text)
    print('Attribute', item.get("x"))
