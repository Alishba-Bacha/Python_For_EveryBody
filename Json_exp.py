import json
data = '''{
    "name" : "Chuck",
    "Phone":{
        "type" : "intl",
        "number": "+1 734 303 4456"
    },
    "email" : {
        "hide": "yes"
    }
}'''
info = json.loads(data)
print('name:', info["name"])
#print('number:',info["phone"]["number"])
print('hide:',info["email"]["hide"])