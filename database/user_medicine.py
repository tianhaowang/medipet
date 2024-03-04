import mysql.connector
import database.connect_db as db

def get_medicine_from_user(user_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT medicine_id FROM user_medicine WHERE user_id = {user_id}"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()

        if not result:
            return "No user_medicine records found."
        else:
            return result

    except Exception as e:
        return f"Error while retrieving user_medicine record(s): {e}"

    finally:
        cursor.close()
        connection.close()

def get_user_from_medicine(medicine_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT user_id FROM user_medicine WHERE medicine_id = {medicine_id}"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()

        if not result:
            return "No user_medicine records found."
        else:
            return result

    except Exception as e:
        return f"Error while retrieving user_medicine record(s): {e}"

    finally:
        cursor.close()
        connection.close()

def create_user_medicine(medicine_id, user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO user_medicine (medicine_id, user_id) VALUES (%s, %s)"
    values = (medicine_id, user_id)

    try:
        cursor.execute(insert_query, values)
        connection.commit()
        return "User_medicine record created successfully."
    except Exception as e:
        return f"Error while creating user_medicine record: {e}"
    finally:
        cursor.close()
        connection.close()

def get_user_medicine(user_medicine_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    if user_medicine_id is None:
        select_query = "SELECT * FROM user_medicine"
        values = None
    else:
        select_query = "SELECT * FROM user_medicine WHERE id = %s"
        values = (user_medicine_id,)

    try:
        if values:
            cursor.execute(select_query, values)
        else:
            cursor.execute(select_query)
        result = cursor.fetchall()

        if not result:
            return "No user_medicine records found."
        else:
            return result
    except Exception as e:
        return f"Error while retrieving user_medicine record(s): {e}"
    finally:
        cursor.close()
        connection.close()

def update_user_medicine(user_medicine_id, condition_id, user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = "UPDATE user_medicine SET condition_id=%s, user_id=%s WHERE id=%s"
    values = (condition_id, user_id, user_medicine_id)

    try:
        cursor.execute(update_query, values)
        connection.commit()
        return "User_medicine record updated successfully."
    except Exception as e:
        return f"Error while updating user_medicine record: {e}"
    finally:
        cursor.close()
        connection.close()

def delete_user_medicine(user_medicine_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = "DELETE FROM user_medicine WHERE id = %s"
    values = (user_medicine_id,)

    try:
        cursor.execute(delete_query, values)
        connection.commit()
        return "User_medicine record deleted successfully."
    except Exception as e:
        return f"Error while deleting user_medicine record: {e}"
    finally:
        cursor.close()
        connection.close()
