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

def test_create_medicine():
    url = f"{url_base}/medicines"  # Use the base URL

    medicine_data = {
        "name": "Paracetamol",
        "description": "Pain relief",
        "recommended_dosage": "500mg every 6 hours"
    }

    response = requests.post(url, json=medicine_data)
    handle_response(response)
    return response.json()['medicine_id']

def test_get_medicine(medicine_id):
    url = f"{url_base}/medicines"  # Use the base URL

    response = requests.patch(url, json={"id": medicine_id})
    handle_response(response)

def test_update_medicine(medicine_id):
    url = f"{url_base}/medicines"  # Use the base URL

    medicine_data = {
        "id": medicine_id,
        "name": "Ibuprofen",
        "description": "Pain and inflammation relief",
        "recommended_dosage": "200mg every 4 hours"
    }

    response = requests.put(url, json=medicine_data)
    handle_response(response)

def test_delete_medicine(medicine_id):
    url = f"{url_base}/medicines"  # Use the base URL

    response = requests.delete(url, json={"id": medicine_id})
    handle_response(response)

def test_get_all_medicines():
    url = f"{url_base}/medicines/all"  # Use the base URL

    handle_response(requests.patch(url))

if __name__ == "__main__":
    # Create a new medicine
    print("Testing medicine creation:")
    medicine_id = test_create_medicine()

    # Retrieve a specific medicine
    print("\nTesting getting a medicine:")
    test_get_medicine(medicine_id)

    # Update a specific medicine
    print("\nTesting updating a medicine:")
    test_update_medicine(medicine_id)

    # Retrieve all medicines
    print("\nTesting getting all medicines:")
    test_get_all_medicines()

    # Delete a specific medicine
    print("\nTesting deleting a medicine:")
    test_delete_medicine(medicine_id)

    # Retrieve all medicines
    print("\nTesting getting all medicines:")
    test_get_all_medicines()
