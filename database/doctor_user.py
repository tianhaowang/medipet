import database.connect_db as db

def create_doctor_user(doctor_id, user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    # Check if the doctor_user association already exists
    check_query = f"SELECT * FROM doctor_user WHERE doctor_id = '{doctor_id}' AND user_id = '{user_id}'"
    try:
        cursor.execute(check_query)
        existing_data = cursor.fetchall()
        if existing_data:
            return None

        # Insert new association since it doesn't exist yet
        insert_query = f"INSERT INTO doctor_user (doctor_id, user_id) VALUES ('{doctor_id}', '{user_id}')"
        cursor.execute(insert_query)
        connection.commit()

        if cursor.rowcount > 0:
            # Re-fetch and return the newly created record for confirmation
            cursor.execute(check_query)  # Reuse the check_query to fetch the newly created record
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while creating or retrieving doctor-user association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()



def get_doctor_by_user(user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT doctor_id FROM doctor_user WHERE user_id = '{user_id}'"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            # Since a user might be associated with multiple doctors, 
            # we're returning a list of all associated doctors' IDs.
            return [item[0] for item in result]
    except Exception as e:
        print(f"Error while retrieving doctor from user ID: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_users_by_doctor(doctor_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT user_id FROM doctor_user WHERE doctor_id = '{doctor_id}'"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            # Since a doctor might be associated with multiple users, 
            # we're returning a list of all associated users' IDs.
            return [item[0] for item in result]
    except Exception as e:
        print(f"Error while retrieving users from doctor ID: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_doctor_in_doctor_user(doctor_user_id, new_doctor_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE doctor_user SET doctor_id='{new_doctor_id}' WHERE id={doctor_user_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM doctor_user WHERE id = '{doctor_user_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating doctor-user association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_user_in_doctor_user(doctor_user_id, new_user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE doctor_user SET user_id='{new_user_id}' WHERE id={doctor_user_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM doctor_user WHERE id = '{doctor_user_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating doctor-user association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def delete_doctor_user(doctor_user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM doctor_user WHERE id = '{doctor_user_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "Doctor-user association deleted successfully."
    except Exception as e:
        print(f"Error while deleting doctor-user association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def delete_relation(doctor_id, user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM doctor_user WHERE doctor_id = '{doctor_id}' and user_id = '{user_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "Doctor-user association deleted successfully."
    except Exception as e:
        print(f"Error while deleting doctor-user association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
