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

def test_create_doctor_user():
    url = f"{url_base}/doctor_user"  # Use the base URL
    data = {"doctor_id": 11, "user_id": 12}
    response = requests.post(url, json=data)
    handle_response(response)
    return response.json()['id']

def test_get_doctor_by_user():
    url = f"{url_base}/doctor_user/doctor"  # Use the base URL
    data = {"user_id": 12}
    response = requests.patch(url, json=data)
    handle_response(response)

def test_get_users_by_doctor():
    url = f"{url_base}/doctor_user/user"  # Use the base URL
    data = {"doctor_id": 11}
    response = requests.patch(url, json=data)
    handle_response(response)

def test_update_doctor_in_doctor_user(doctor_id):
    url = f"{url_base}/doctor_user/doctor"  # Use the base URL
    data = {"id": doctor_id, "doctor_id": 17}
    response = requests.put(url, json=data)
    handle_response(response)

def test_update_user_in_doctor_user(doctor_id):
    url = f"{url_base}/doctor_user/user"  # Use the base URL
    data = {"id": doctor_id, "user_id": 17}
    response = requests.put(url, json=data)
    handle_response(response)

def test_delete_doctor_user(doctor_id):
    url = f"{url_base}/doctor_user"  # Use the base URL
    data = {"id": doctor_id}
    response = requests.delete(url, json=data)
    handle_response(response)

if __name__ == "__main__":
    print("Testing creating doctor-user:")
    doctor_id = test_create_doctor_user()

    print("\nTesting getting doctor by user:")
    test_get_doctor_by_user()

    print("\nTesting getting users by doctor:")
    test_get_users_by_doctor()

    print("\nTesting updating doctor in doctor-user:")
    test_update_doctor_in_doctor_user(doctor_id)

    print("\nTesting updating user in doctor-user:")
    test_update_user_in_doctor_user(doctor_id)

    print("\nTesting deleting doctor-user:")
    test_delete_doctor_user(doctor_id)
