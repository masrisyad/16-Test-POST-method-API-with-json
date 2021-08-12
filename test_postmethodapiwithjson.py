import requests
import json

# test by risyad abdala ramadhan

url = 'https://api.trello.com/1/boards/'

file = open('C:\Automation script\Test POST method API with json\post.json', 'r')

request_json = json.loads(file.read())

response = requests.post(url,json=request_json)

# cetak response code

print(response.status_code)

# cetak json file

json_response = json.loads(response.text)

print(json_response)