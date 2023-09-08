#Retrieving links from a link   exp:https://py4e-data.dr-chuck.net/known_by_Martin.html
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url ')
count = int(input('Enter count'))
position = int(input('Enter position'))-1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,"html.parser")

seq = list()
# Retrieve all of the anchor tags
href = soup('a')
for i  in range(count):
    link = href[position].get('href', None)
    print('Retrieving', link)
    #lines = ('Contents:', tag.contents[0])
    seq.append(href[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
    link = href[position].get('href', None)
print(seq[-1])