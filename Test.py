import requests

response = requests.get(url="https://www.google.com")

if response.status_code == 200:
    print("Response Exitosa")
else:
    print("No se pudo realizar el response")