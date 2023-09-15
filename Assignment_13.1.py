#Sum the numbers in an XML data retrieved from a url
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url).read()
print('Retrieved', len(uh), 'characters')
sum = 0
count = 0

tree = ET.fromstring(uh)
results = tree.findall('comments/comment')
for c in results:
    count = count + 1
    num = c.find('count').text
    sum = sum + float(num)
    
print ('Count:', count)
print ('Sum:' , sum)