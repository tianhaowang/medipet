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

def test_create_schedule():
    url = f"{url_base}/schedule"  # Use the base URL
    data = {"user_id": 12, "medicine_id": 5, "time": "09:00:00", "taken": False}
    response = requests.post(url, json=data)
    handle_response(response)
    return response.json()['id']

def test_get_schedule(id):
    url = f"{url_base}/schedule"  # Use the base URL
    data = {"id": id}
    response = requests.patch(url, json=data)
    handle_response(response)

def test_update_taken_in_schedule(id):
    url = f"{url_base}/schedule"  # Use the base URL
    data = {"id": id, "taken": True}
    response = requests.put(url, json=data)
    handle_response(response)

def test_delete_schedule(id):
    url = f"{url_base}/schedule"  # Use the base URL
    data = {"id": id}
    response = requests.delete(url, json=data)
    handle_response(response)

if __name__ == "__main__":
    print("Testing creating schedule:")
    id = test_create_schedule()

    print("\nTesting getting schedule by ID:")
    test_get_schedule(id)

    print("\nTesting updating 'taken' in schedule:")
    test_update_taken_in_schedule(id)

    print("\nTesting deleting schedule:")
    test_delete_schedule(id)
