from database.schedule import create_schedule, update_taken_in_schedule, get_schedule, delete_schedule

# Replace these values with actual data to test the functions
test_user_id = 6
test_medicine_id = 5
test_time = '09:00:00'
test_taken = 0

# Test create_schedule function
created_schedule = create_schedule(test_user_id, test_medicine_id, test_time, test_taken)
print("New schedule created:", created_schedule)

# Test update_taken_in_schedule function with a specific schedule_id
schedule_id_to_update = created_schedule[0][0]  # Replace this with the ID of the schedule you want to update
new_taken_status = 1
updated_schedule = update_taken_in_schedule(schedule_id_to_update, new_taken_status)
print("Updated taken status in schedule:", updated_schedule)

# Test get_schedule function with a specific schedule_id
schedule_id_to_retrieve = schedule_id_to_update
retrieved_schedule = get_schedule(schedule_id_to_retrieve)
print("Retrieved schedule:", retrieved_schedule)

# Test delete_schedule function with a specific schedule_id
schedule_id_to_delete = created_schedule[0][0]  # Replace this with the ID of the schedule you want to delete
delete_result = delete_schedule(schedule_id_to_delete)
print("Delete result:", delete_result)
