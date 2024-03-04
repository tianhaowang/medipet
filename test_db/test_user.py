from database.users import create_user, get_user, update_user, delete_user, get_all_users

# Replace these values with actual data to test the functions
test_username = "test_user"
test_password = "test_password"
test_firstname = "John"
test_lastname = "Doe"
test_email = "john.doe@example.com"
test_phone = "123-456-7890"
test_address = "123 Main Street, City"

# Test create_user function
new_user = create_user(test_username, test_password, test_firstname, test_lastname, test_email, test_phone, test_address)
print("New user created:", new_user)
print("New user created:", new_user[0][0])


# Test get_user function with a specific user_id (replace user_id with a valid ID)
user_id_to_retrieve = new_user[0][0]
retrieved_user = get_user(user_id_to_retrieve)
print("Retrieved user by ID:", retrieved_user)

# Test update_user function with a specific user_id (replace user_id with a valid ID)
user_id_to_update = new_user[0][0]
updated_user = update_user(user_id_to_update, test_username, "new_password", test_firstname, test_lastname, test_email, test_phone, test_address)
print("Updated user:", updated_user)

# Test get_all_users function
all_users = get_all_users()
print("All users retrieved:", all_users)

# Test delete_user function with a specific user_id (replace user_id with a valid ID)
user_id_to_delete = new_user[0][0]
delete_result = delete_user(user_id_to_delete)
print("Delete result:", delete_result)

# Test get_all_users function
all_users = get_all_users()
print("All users retrieved:", all_users)