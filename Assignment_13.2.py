#THis programm look for count in comments summ all counts and count all comments
import urllib.request, urllib.parse, urllib.error
import json

#link used is http://py4e-data.dr-chuck.net/comments_1833347.json

count = 0
sum = 0

link = input('Enter url- ')

print('Retrieving Url:', link)
with urllib.request.urlopen(link)as url:
    data = json.loads(url.read().decode())
print('Retrieved', len(data), "Characters")
data_1 = data.get("comments")

for j in range(len(data_1)):
    count = count + 1
    x = data_1[j].get("count")
    z = int(x)
    sum = sum + z
print("count:",count)
print("Sum:",sum)