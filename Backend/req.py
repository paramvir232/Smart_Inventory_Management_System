import requests

url = 'http://127.0.0.1:5000/product/add_product'
jwt_token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoxMjQ2LCJleHAiOjE3Mzk4MTczODN9.T5m_QKwjWCSRS4ix_idAXwhZ2_MpBPbLX2ACodm20xc'
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json"
}
# response = requests.get(url,headers=headers)
response = requests.post(url,json={
           "productId":123, 
           "productName": "Updated Product Name",
           "productPrice": 29.99,
           "productStock": 100,
           "delivered_date": "2023-10-01",
           "next_delivery_date": "2023-10-15",
           "productDefaultOrder": 20,
           "productSold": 10,
           "productStatus": "Available"
         })
# response = requests.delete(url+'/7')

print(response.json())


