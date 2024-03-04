from database.conditions import create_condition, get_condition, update_condition, delete_condition, get_all_conditions

# Replace these values with actual data to test the functions
test_condition_name = "TestCondition"

# Test create_condition function
created_condition = create_condition(test_condition_name)
print("New condition created:", created_condition)

# Test get_condition function with a specific condition_id (replace condition_id with a valid ID)
condition_id_to_retrieve = created_condition[0][0]  # Replace this with the ID of the condition you want to retrieve
retrieved_condition = get_condition(condition_id_to_retrieve)
print("Retrieved condition by ID:", retrieved_condition)

# Test update_condition function with a specific condition_id (replace condition_id with a valid ID)
condition_id_to_update = created_condition[0][0]  # Replace this with the ID of the condition you want to update
updated_condition = update_condition(condition_id_to_update, "UpdatedConditionName")
print("Updated condition:", updated_condition)

# Test get_condition function without passing a condition_id (should retrieve all conditions)
all_conditions = get_all_conditions()
print("All conditions retrieved:", all_conditions)
      
# Test delete_condition function with a specific condition_id (replace condition_id with a valid ID)
condition_id_to_delete = created_condition[0][0]  # Replace this with the ID of the condition you want to delete
delete_result = delete_condition(condition_id_to_delete)
print("Delete result:", delete_result)

# Test get_condition function without passing a condition_id (should retrieve all conditions)
all_conditions = get_all_conditions()
print("All conditions retrieved:", all_conditions)
