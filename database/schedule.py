import database.connect_db as db
import sys 

def create_schedule(user_id, medicine_id, time, taken, dosage):
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO schedule (user_id, medicine_id, time, taken, dosage) VALUES (%s, %s, %s, %s, %s)"
    insert_values = (user_id, medicine_id, time, taken, dosage)

    try:
        cursor.execute(insert_query, insert_values)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM schedule WHERE user_id = '{user_id}' and medicine_id = '{medicine_id}' and time = '{time}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while creating schedule: {e}", file=sys.stderr)
        return None
    finally:
        cursor.close()
        connection.close()


def update_taken_in_schedule(schedule_id, taken):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE schedule SET taken={taken} WHERE id={schedule_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM schedule WHERE id = '{schedule_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating taken status in schedule: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_schedule(user_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM schedule WHERE user_id = '{user_id}'"

    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving schedule: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def delete_schedule(schedule_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM schedule WHERE id = '{schedule_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "Schedule deleted successfully."
    except Exception as e:
        print(f"Error while deleting schedule: {e}")
        return None
    finally:
        cursor.close()
        connection.close()
