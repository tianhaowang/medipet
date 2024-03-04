from database.user_conditions import create_user_condition, get_condition_by_user, get_users_by_condition, update_condition_in_user_condition, update_user_in_user_condition, delete_user_condition

# Replace these values with actual data to test the functions
test_condition_id = 4
test_user_id = 6

# Test create_user_condition function
created_user_condition = create_user_condition(test_condition_id, test_user_id)
print("New user-condition created:", created_user_condition)

# Test get_condition_by_user function with a specific user_id
user_id_to_retrieve = test_user_id
retrieved_condition = get_condition_by_user(user_id_to_retrieve)
print("Retrieved condition by user ID:", retrieved_condition)

# Test get_users_by_condition function with a specific condition_id
condition_id_to_retrieve = test_condition_id
retrieved_users = get_users_by_condition(condition_id_to_retrieve)
print("Retrieved users by condition ID:", retrieved_users)

# Test update_condition_in_user_condition function with a specific user_condition_id (replace user_condition_id with a valid ID)
user_condition_id_to_update = created_user_condition[0][0]  # Replace this with the ID of the user-condition you want to update
new_condition_id = 10
updated_user_condition = update_condition_in_user_condition(user_condition_id_to_update, new_condition_id)
print("Updated condition in user-condition:", updated_user_condition)

# Test update_user_in_user_condition function with a specific user_condition_id (replace user_condition_id with a valid ID)
new_user_id = 5
updated_user_condition = update_user_in_user_condition(user_condition_id_to_update, new_user_id)
print("Updated user in user-condition:", updated_user_condition)

# Test delete_user_condition function with a specific user_condition_id (replace user_condition_id with a valid ID)
user_condition_id_to_delete = created_user_condition[0][0]  # Replace this with the ID of the user-condition you want to delete
delete_result = delete_user_condition(user_condition_id_to_delete)
print("Delete result:", delete_result)
