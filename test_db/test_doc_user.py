from database.doctor_user import create_doctor_user, get_doctor_by_user, get_users_by_doctor, update_doctor_in_doctor_user, update_user_in_doctor_user, delete_doctor_user

# Replace these values with actual data to test the functions
test_doctor_id = 8
test_user_id = 2

# Test create_doctor_user function
for i in range(5):
    created_doctor_user = create_doctor_user(test_doctor_id, 10+i)
    print("New doctor-user created:", created_doctor_user)

# # Test get_doctor_by_user function with a specific user_id
# user_id_to_retrieve = test_user_id
# retrieved_doctor = get_doctor_by_user(user_id_to_retrieve)
# print("Retrieved doctor by user ID:", retrieved_doctor)

# # Test get_users_by_doctor function with a specific doctor_id
# doctor_id_to_retrieve = test_doctor_id
# retrieved_users = get_users_by_doctor(doctor_id_to_retrieve)
# print("Retrieved users by doctor ID:", retrieved_users)

# # Test update_doctor_in_doctor_user function with a specific doctor_user_id (replace doctor_user_id with a valid ID)
# doctor_user_id_to_update = created_doctor_user[0][0]  # Replace this with the ID of the doctor-user you want to update
# new_doctor_id = 4
# updated_doctor_user = update_doctor_in_doctor_user(doctor_user_id_to_update, new_doctor_id)
# print("Updated doctor in doctor-user:", updated_doctor_user)

# # Test update_user_in_doctor_user function with a specific doctor_user_id (replace doctor_user_id with a valid ID)
# new_user_id = 5
# updated_doctor_user = update_user_in_doctor_user(doctor_user_id_to_update, new_user_id)
# print("Updated user in doctor-user:", updated_doctor_user)

# # Test delete_doctor_user function with a specific doctor_user_id (replace doctor_user_id with a valid ID)
# doctor_user_id_to_delete = created_doctor_user[0][0]  # Replace this with the ID of the doctor-user you want to delete
# delete_result = delete_doctor_user(doctor_user_id_to_delete)
# print("Delete result:", delete_result)
