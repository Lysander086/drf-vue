import requests

from clients.clients import config

def client():
    credentials = {"username": "admin", "password": config.admin_password} # shall define your own password hereapi/rest-auth
    response = requests.post("http://localhost:8000/api/rest-auth/login/", data=credentials)

    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()