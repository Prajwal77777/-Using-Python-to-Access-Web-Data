import urllib.request
import json
URL = input("Enter Location: ")
response = urllib.request.urlopen(URL)
data = response.read().decode()

json_data = json.loads(data)


comments = json_data["comments"]

counts = [comment["count"]for comment in comments]
Sum = sum(counts)
print(f"Print:{Sum}")
