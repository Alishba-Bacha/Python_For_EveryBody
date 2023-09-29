#Retrieving data from xml
import xml.etree.ElementTree as ET
data = '''<person>
    <name>Chuck</name>
    <phone type = "intl">
        +1 73 303 4456
    </phone>
    <email hide = "yes"/>
</person> '''  #triple quoted string is a multi line string in python

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('phone:', tree.find('phone').text)
print('Attr:', tree.find('email').get('hide'))