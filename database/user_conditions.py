import database.connect_db as db

def create_user_condition(condition_id, user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    insert_query = f"INSERT INTO user_condition (condition_id, user_id) VALUES ('{condition_id}', '{user_id}')"

    try:
        cursor.execute(insert_query)
        connection.commit()
        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM user_condition WHERE condition_id = '{condition_id}' and user_id = '{user_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while creating user-condition association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_condition_by_user(user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT condition_id FROM user_condition WHERE user_id = '{user_id}'"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            # Since a user might have multiple conditions, 
            # we're returning a list of all associated conditions' IDs.
            return [item[0] for item in result]
    except Exception as e:
        print(f"Error while retrieving condition from user ID: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_users_by_condition(condition_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT user_id FROM user_condition WHERE condition_id = '{condition_id}'"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            # Since a condition might be associated with multiple users, 
            # we're returning a list of all associated users' IDs.
            return [item[0] for item in result]
    except Exception as e:
        print(f"Error while retrieving users from condition ID: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_condition_in_user_condition(user_condition_id, new_condition_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE user_condition SET condition_id='{new_condition_id}' WHERE id={user_condition_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM user_condition WHERE id = '{user_condition_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating user-condition association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_user_in_user_condition(user_condition_id, new_user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE user_condition SET user_id='{new_user_id}' WHERE id={user_condition_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM user_condition WHERE id = '{user_condition_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating user-condition association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def delete_user_condition(user_condition_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM user_condition WHERE id = '{user_condition_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "User-condition association deleted successfully."
    except Exception as e:
        print(f"Error while deleting user-condition association: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
