import requests

url = 'http://127.0.0.1:5000/login'
jwt_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoxMjQ2LCJleHAiOjE3Mzk4MTczODN9.T5m_QKwjWCSRS4ix_idAXwhZ2_MpBPbLX2ACodm20xc'
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}

response = requests.get(url)


print(response.text)


