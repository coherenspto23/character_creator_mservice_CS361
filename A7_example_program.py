import requests

#this is for post
service_url = "http://localhost:5003/api/character/create"

#test
data = {
    "name": "Callipso"
}

response = requests.post(service_url, json = data)
print(response.json())

#this is for get
get_request = requests.get("http://localhost:5003/api/character/name")
print(get_request.json())