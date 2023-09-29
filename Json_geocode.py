#Retrieving address from an API generally and longitude and latitude of the location line Mardan etc
import urllib.request, urllib.parse, urllib.error
import json
serviceUrl = 'https://py4e-data.dr-chuck.net/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    url = serviceUrl + urllib.parse.urlencode({'address': address})
    print('Retrieving Url:', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), "Characters")
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js['status'] != 'OK':
        print(data)
        continue

    print(json.dumps(js, indent = 4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js["results"][0]["formatted_address"]
    print(location)