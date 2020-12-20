import requests

from clients.clients import config

def check_admin_login():
    credentials = {"username": "admin", "password": config.admin_password} # shall define your own password hereapi/rest-auth
    response = requests.post("http://localhost:8000/api/rest-auth/login/", data=credentials) # must end with slash

    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)


def client():
    response = requests.get("http://localhost:8000/api/profiles")
    print("Status Code : ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    # check_admin_login()
    client()