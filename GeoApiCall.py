import urllib.request
import json
import urllib.parse


location = input("Enter the location: ")

base_url = "http://py4e-data.dr-chuck.net/json?"

parameters = {"address": location, "key": 42}

url = base_url + urllib.parse.urlencode(parameters)


response = urllib.request.urlopen(url)

data = response.read().decode()
json_data = json.loads(data)

place_id = json_data["results"][0]["place_id"]


print(f"place_id: {place_id}")
