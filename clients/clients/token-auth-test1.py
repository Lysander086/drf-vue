import requests

from .config import admin_password

def client():
    credentials = {"username": "admin", "password": admin_password} # shall define your own password here
    response = requests.post("http://localhost:8000/api/rest-auth/login", data=credentials)

    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()