from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
count = dict()
sum = 0

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#retrieve all anchor tags
tags = soup('span')
for tag in tags:
      count[tag] = count.get(tag, 0) + 1
      lines = ('Contents:', tag.contents[0])
      num = list(lines)
      y = int(num[1])
      if y > 0:
            sum = sum + y
print("count", count)
print("sum", sum)

