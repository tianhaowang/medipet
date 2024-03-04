import database.connect_db as db

def create_condition(name):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    insert_query = f"INSERT INTO conditions (name) VALUES ('{name}')"

    try:
        cursor.execute(insert_query)
        connection.commit()
        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM conditions WHERE name = '{name}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while creating condition record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def get_condition(condition_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM conditions WHERE id = '{condition_id}'"

    try:
        if select_query:
            cursor.execute(select_query)
            result = cursor.fetchall()
            if not result:
                return None
            else:
                return result
    except Exception as e:
        print(f"Error while retrieving condition record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def get_all_conditions():
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = "SELECT * FROM conditions"

    try:
        cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving all condition records: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def update_condition(condition_id, name):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE conditions SET name='{name}' WHERE id={condition_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM conditions WHERE id = '{condition_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating condition record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def delete_condition(condition_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM conditions WHERE id = '{condition_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "Condition record deleted successfully."
    except Exception as e:
        print(f"Error while deleting condition record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
