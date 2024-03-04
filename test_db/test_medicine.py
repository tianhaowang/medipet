from database.medicine import create_medicine, get_medicine, update_medicine, delete_medicine, get_all_medicines

# Replace these values with actual data to test the functions
test_medicine_name = "Test Medicine"
test_description = "This is a test description"
test_recommended_dosage = "10mg"

# Test create_medicine function
new_medicine = create_medicine(test_medicine_name, test_description, test_recommended_dosage)
print("New medicine created:", new_medicine)
print("New medicine created:", new_medicine[0][0])

# Test get_medicine function with a specific medicine_id (replace medicine_id with a valid ID)
medicine_id_to_retrieve = new_medicine[0][0]
retrieved_medicine = get_medicine(medicine_id_to_retrieve)
print("Retrieved medicine by ID:", retrieved_medicine)

# Test update_medicine function with a specific medicine_id (replace medicine_id with a valid ID)
medicine_id_to_update = new_medicine[0][0]
updated_medicine = update_medicine(medicine_id_to_update, test_medicine_name, "updated description", "20mg")
print("Updated medicine:", updated_medicine)

# Test get_all_medicines function
all_medicines = get_all_medicines()
print("All medicines retrieved:", all_medicines)

# Test delete_medicine function with a specific medicine_id (replace medicine_id with a valid ID)
medicine_id_to_delete = new_medicine[0][0]
delete_result = delete_medicine(medicine_id_to_delete)
print("Delete result:", delete_result)

# Test get_all_medicines function
all_medicines = get_all_medicines()
print("All medicines retrieved:", all_medicines)
