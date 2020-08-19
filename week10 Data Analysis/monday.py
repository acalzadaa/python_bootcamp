# Monday: Virtual Environments and Requests Module

# sending a request and logging the response code

import requests

r = requests.get("https://api.github.com/users/acalzadaa")
print(r)
print(type(r))

# accessing the content that we requested from the URL

data = r.content
print(data)

# converting data from JSON into a Python dictionary and outputting all key-value pairs

data = r.json()
for k,v in data.items():
    print(f"Key: {k} Value: {v}")
print(data["name"])

# outputting specific key-value pairs from data

r = requests.get("https://api.github.com/search/repositories?q=language:python")
data = r.json()
print(data["total_count"])



url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

data = requests.get(url=url, params=params).json()

for k,v in data.items():
    print(f"Key: {k} Value: {v}")
