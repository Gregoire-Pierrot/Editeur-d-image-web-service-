import requests

data = {
    'username': "test_username",
    'password': "test_password"
}

url = "http://10.120.20.219:5000/add_user"

response = requests.post(url, json=data)

if response.status_code == 200:
    print("c'est bon.")
else:
    print("c'est pas bon ...")