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

def test_create_user_condition():
    url = f"{url_base}/user_condition"
    data = {"condition_id": 9, "user_id": 12}
    response = requests.post(url, json=data)
    handle_response(response)
    return response.json()['id']

def test_get_condition_by_user():
    url = f"{url_base}/user_condition/user"
    data = {"user_id": 12}
    response = requests.patch(url, json=data)
    handle_response(response)

def test_get_users_by_condition():
    url = f"{url_base}/user_condition/condition"
    data = {"condition_id": 9}
    response = requests.patch(url, json=data)
    handle_response(response)

def test_update_condition_in_user_condition(id):
    url = f"{url_base}/user_condition/condition"
    data = {"id": id, "condition_id": 10}
    response = requests.put(url, json=data)
    handle_response(response)

def test_update_user_in_user_condition(id):
    url = f"{url_base}/user_condition/user"
    data = {"id": id, "user_id": 13}
    response = requests.put(url, json=data)
    handle_response(response)

def test_delete_user_condition(id):
    url = f"{url_base}/user_condition"
    data = {"id": id}
    response = requests.delete(url, json=data)
    handle_response(response)

if __name__ == "__main__":
    print("Testing creating user-condition:")
    id = test_create_user_condition()

    print("\nTesting getting condition by user:")
    test_get_condition_by_user()

    print("\nTesting getting users by condition:")
    test_get_users_by_condition()

    print("\nTesting updating condition in user-condition:")
    test_update_condition_in_user_condition(id)

    print("\nTesting updating user in user-condition:")
    test_update_user_in_user_condition(id)

    print("\nTesting deleting user-condition:")
    test_delete_user_condition(id)
