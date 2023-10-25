import requests 

link = 'http://127.0.0.1:5000/API'

req = requests.get(link)

print(req)
print(req.json())