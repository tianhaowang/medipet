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

def create_condition():
    url = f"{url_base}/conditions"  # Use the base URL

    condition_data = {
        "name": "Condition_1"
    }

    response = requests.post(url, json=condition_data)
    handle_response(response)
    return response.json()['condition_id']

def test_get_condition(condition_id):
    url = f"{url_base}/conditions"  # Use the base URL

    response = requests.patch(url, json={"id": condition_id})
    handle_response(response)

def test_update_condition(condition_id):
    url = f"{url_base}/conditions"  # Use the base URL

    updated_data = {
        "id": condition_id,
        "name": "Updated_Condition_1"
    }

    response = requests.put(url, json=updated_data)
    handle_response(response)

def test_delete_condition(condition_id):
    url = f"{url_base}/conditions"  # Use the base URL

    response = requests.delete(url, json={"id": condition_id})
    handle_response(response)

def test_get_all_conditions():
    url = f"{url_base}/conditions/all"  # Use the base URL

    response = requests.patch(url)
    handle_response(response)

if __name__ == "__main__":
    condition_id = create_condition()
    test_get_condition(condition_id)
    test_update_condition(condition_id)
    test_get_condition(condition_id)  # Add to verify the condition was updated correctly
    test_delete_condition(condition_id)
    test_get_all_conditions()  # It should be empty now since we deleted the condition
