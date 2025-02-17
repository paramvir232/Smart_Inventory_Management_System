import requests

url = 'http://127.0.0.1:5000/auth/login'
response = requests.post(url,json= {
        'storeId':126,
        'storePassword':"hi"})
# response = requests.get(url)
# response = requests.delete(url+'/7')

print(response.json())


