import database.connect_db as db

def create_child(parent_id, points, hunger, happiness, health, alert_threshold, miss_threshold):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    # Adjusted to new table structure and fields
    insert_query = """
    INSERT INTO children (Parent_id, Points, Hunger, Happiness, Health, Alert_threshold, Miss_threshold) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    try:
        # Execute the insert query
        cursor.execute(insert_query, (parent_id, points, hunger, happiness, health, alert_threshold, miss_threshold))
        connection.commit()

        # Check if a new row was inserted
        if cursor.rowcount > 0:
            child_id = cursor.lastrowid
            # Fetch the newly created child record
            select_query = f"SELECT * FROM children WHERE id = {child_id}"
            cursor.execute(select_query)
            new_child = cursor.fetchone()
            return new_child
        else:
            return None
    except Exception as e:
        print(f"Error while creating child record: {e}")
        return None
    finally:
        # Ensure resources are freed
        cursor.close()
        connection.close()


def get_child_by_parent_id(parent_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    # Query to fetch all data related to the child based on the parent's ID
    query = """
    SELECT 
        children.*,
        users.username AS parent_username, users.firstname AS parent_firstname, users.lastname AS parent_lastname, 
        users.email AS parent_email, users.phone AS parent_phone, users.address AS parent_address, users.active AS parent_active,
        GROUP_CONCAT(DISTINCT CONCAT(schedule.time, ' - ', medicine.name, ' - ', IF(schedule.taken, 'Taken', 'Not taken'))) AS medicine_schedule
    FROM 
        children
    LEFT JOIN 
        users ON children.Parent_id = users.id
    LEFT JOIN 
        schedule ON users.id = schedule.user_id
    LEFT JOIN 
        medicine ON schedule.medicine_id = medicine.id
    WHERE 
        children.Parent_id = %s
    GROUP BY 
        children.id;
    """

    try:
        # Execute the query
        cursor.execute(query, (parent_id,))
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving child data: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


# Inside your db_children module

def update_child(id, points=None, hunger=None, happiness=None, health=None, alert_threshold=None, miss_threshold=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    # Constructing the update query dynamically based on provided fields
    fields_to_update = []
    
    if points is not None:
        fields_to_update.append(f"Points = {points}")
    if hunger is not None:
        fields_to_update.append(f"Hunger = {hunger}")
    if happiness is not None:
        fields_to_update.append(f"Happiness = {happiness}")
    if health is not None:
        fields_to_update.append(f"Health = {health}")
    if alert_threshold is not None:
        fields_to_update.append(f"Alert_threshold = {alert_threshold}")
    if miss_threshold is not None:
        fields_to_update.append(f"Miss_threshold = {miss_threshold}")
    
    update_query = "UPDATE children SET " + ", ".join(fields_to_update) + f" WHERE id = {id}"
    
    try:
        cursor.execute(update_query)
        connection.commit()
        if cursor.rowcount > 0:
            return True  # Successfully updated
        else:
            return False  # No record found to update
    except Exception as e:
        print(f"Error while updating child record: {e}")
        return False
    finally:
        cursor.close()
        connection.close()
