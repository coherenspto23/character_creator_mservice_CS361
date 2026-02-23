import requests

#this is for post
service_url = "http://localhost:5003/api/character/create"

#test
data = {
    "name": "Callipso",
    "equipped_items": "top_hat"
}

response = requests.post(service_url, json = data)
print(response.json())

