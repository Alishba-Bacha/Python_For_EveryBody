import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
ist = stuff.findall('users/user')   #All user tags below users  and  ist is list of tags
print('User count:',len(ist))
for item in ist :
    print('Name', item.find('name').text)
    print('ID', item.find('id').text)
    print('Attribute:',item.get("x"))

