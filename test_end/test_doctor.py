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

def test_create_doctor():
    url = f"{url_base}/doctors"  # Use the base URL

    doctor_data = {
        "username": "t23ianh12313o1232123",
        "password": "pass23w1231123ord123",
        "firstname": "John",
        "lastname": "Doe",
        "email": "tianh212313ao12312123.doe@exasdaample.com",
        "phone": "991231231321239123819123",
        "address": "123 Main St",
        "specialization": "Cardiology"
    }

    response = requests.post(url, json=doctor_data)
    handle_response(response)
    return response.json()['doctor_id']

def test_get_doctor(doctor_id):
    url = f"{url_base}/doctors"  # Use the base URL

    doctor_id = doctor_id  # Replace this with the doctor ID you want to test

    response = requests.patch(url, json={"id": doctor_id})
    handle_response(response)

def test_update_doctor(doctor_id):
    url = f"{url_base}/doctors"  # Use the base URL

    data = {
        "id": doctor_id,
        "username": "new1231_do1231ctor_username",
        "password": "ne123w_p12312313assword",
        "firstname": "John",
        "lastname": "Doe",
        "email": "doc123123tor.doe@ex123123ample.com",
        "phone": "12341231231356789",
        "address": "123 Main Street",
        "specialization": "Neurology"
    }

    response = requests.put(url, json=data)
    handle_response(response)

def test_delete_doctor(doctor_id):
    url = f"{url_base}/doctors"  # Use the base URL

    data = {
        "id": doctor_id
    }

    response = requests.delete(url, json=data)
    handle_response(response)

def test_get_all_doctors():
    url = f"{url_base}/doctors/all"  # Use the base URL

    handle_response(requests.patch(url))

if __name__ == "__main__":
    # Create a new doctor
    print("Testing doctor creation:")
    doctor_id = test_create_doctor()

    # Retrieve a specific doctor
    print("\nTesting getting a doctor:")
    test_get_doctor(doctor_id)

    # Update a specific doctor
    print("\nTesting updating a doctor:")
    test_update_doctor(doctor_id)

    # Retrieve all doctors
    print("\nTesting getting all doctors:")
    test_get_all_doctors()

    # Delete a specific doctor
    print("\nTesting deleting a doctor:")
    test_delete_doctor(doctor_id)
