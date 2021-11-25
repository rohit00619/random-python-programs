import xml.etree.ElementTree as ET
data = '''<person>
    <name>chuck</name>
    <Phone type = "intl"> +918871796876 </phone>
    <email hide="yes"/>
    </person>'''

    tree = ET.fromstring(data)
    print('Name:', tree.find('name').text)
    print('Attr:', tree.find('email').get('hide'))
