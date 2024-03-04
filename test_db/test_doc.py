from database.doctor import create_doctor, get_doctor, get_all_doctors, update_doctor, delete_doctor

# Replace these values with actual data to test the functions
test_doctor_data = {
    'username': 'TestUsername',
    'password': 'TestPassword',
    'firstname': 'TestFirstName',
    'lastname': 'TestLastName',
    'email': 'test@example.com',
    'phone': '1234567890',
    'address': '123 Test Street, Test City, 12345',
    'medical_license': 'TestMedicalLicense'
}

# Test create_doctor function
created_doctor = create_doctor(**test_doctor_data)
print("New doctor created:", created_doctor)

# Test get_doctor function with a specific doctor_id (replace doctor_id with a valid ID)
doctor_id_to_retrieve = created_doctor[0][0]  # Replace this with the ID of the doctor you want to retrieve
retrieved_doctor = get_doctor(doctor_id_to_retrieve)
print("Retrieved doctor by ID:", retrieved_doctor)

# Test update_doctor function with a specific doctor_id (replace doctor_id with a valid ID)
doctor_id_to_update = created_doctor[0][0]  # Replace this with the ID of the doctor you want to update
updated_doctor_data = test_doctor_data.copy()
updated_doctor_data['username'] = "UpdatedUsername"
updated_doctor = update_doctor(doctor_id_to_update, **updated_doctor_data)
print("Updated doctor:", updated_doctor)

# Test get_all_doctors function (should retrieve all doctors)
all_doctors = get_all_doctors()
print("All doctors retrieved:", all_doctors)
      
# Test delete_doctor function with a specific doctor_id (replace doctor_id with a valid ID)
doctor_id_to_delete = created_doctor[0][0]  # Replace this with the ID of the doctor you want to delete
delete_result = delete_doctor(doctor_id_to_delete)
print("Delete result:", delete_result)

# Test get_all_doctors function again (should retrieve all doctors)
all_doctors = get_all_doctors()
print("All doctors retrieved:", all_doctors)
