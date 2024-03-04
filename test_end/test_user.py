import requests
import json

url_base = "http://127.0.0.1:1492" 
# Function to handle the response
def handle_response(response):
    try:
        response_json = response.json()
        print("Response JSON Data:", response_json)
    except json.JSONDecodeError:
        print("Response Text (Not JSON):", response.text)

    print("Response Status Code:", response.status_code)

def create():
    # URL of your Flask app's /create_user endpoint
    url = f"{url_base}/users"

    # Sample user data
    user_data = {
        "username": "tianho12312313",
        "password": "password123",
        "firstname": "John",
        "lastname": "Doe",
        "email": "62342342.doe@example.com",
        "phone": "123-4623456-7890",
        "address": "123 Main St"
    }

    # Make a POST request to the /create_user endpoint
    response = requests.post(url, json=user_data)
    handle_response(response)
    return response.json()['user_id']

def test_get(user_id):
    # URL of your Flask app's /users endpoint
    url = f"{url_base}/users"

    # Make a GET request to the /users endpoint with the user_id as a query parameter
    response = requests.patch(url, json={"id": user_id})
    handle_response(response)

# Test update_user_endpoint
def test_update_user(user_id):
    url = f"{url_base}/users"

    data = {
        "id": user_id,
        "username": "tianhao1231",
        "password": "new_password",
        "firstname": "John",
        "lastname": "Doe",
        "email": "tianhao.doe@example.com",
        "phone": "1234512316789",
        "address": "123 Main Street"
    }

    response = requests.put(url, json=data)
    handle_response(response)

# Test delete_user_endpoint
def test_delete_user(user_id):
    url = f"{url_base}/users"

    data = {
        "id": user_id
    }

    response = requests.delete(url, json=data)
    handle_response(response)

def test_get_all_users():
    # URL of your Flask app's /users/all endpoint
    url = f"{url_base}/users/all"

    # Make a GET request to the /users/all endpoint
    response = requests.patch(url)
    handle_response(response)

if __name__ == "__main__":
    user_id = create()
    test_get(user_id)
    test_update_user(user_id)
    test_delete_user(user_id)
    test_get_all_users()
