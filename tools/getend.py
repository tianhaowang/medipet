import requests

# URL of your Flask app's /users endpoint
url = "http://127.0.0.1:1492/users"

# Sample user ID for testing
user_id = 25  # Replace this with the user ID you want to test

# Make a GET request to the /users endpoint with the user_id as a query parameter
response = requests.patch(url, json={"id": user_id})

# Print the response status code
print("Response Status Code:", response.status_code)

try:
    # Attempt to parse the JSON response data
    json_data = response.json()
    # Print the JSON data if successful
    print("Response JSON Data:", json_data)
except requests.exceptions.JSONDecodeError as e:
    # Print the response content to debug the issue
    print("Failed to parse JSON response:", e)
    print("Response Content:", response.content)
