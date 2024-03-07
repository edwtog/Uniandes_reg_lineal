import requests

url = 'http://127.0.0.1:8000/predict/'
data = {'hours': 5.0}

response = requests.post(url, json=data)
print(response.json())
response.json()
#curl -X POST "http://127.0.0.1:8000/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"hours\": 5.0}"
