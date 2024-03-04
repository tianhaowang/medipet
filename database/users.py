import database.connect_db as db
import boto3
import sys 
import os
\
# S3 credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = 'medibottian'


s3 = boto3.client('s3', 
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name='us-east-2')

def create_user(username, password, firstname, lastname, email, phone, address):
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    insert_query = f"INSERT INTO users (username, password, firstname, lastname, email, phone, address, active) VALUES ('{username}', '{password}', '{firstname}', '{lastname}', '{email}', '{phone}', '{address}', '0')"

    try:
        cursor.execute(insert_query)
        connection.commit()
        # Check if any rows were affected by the update.
        if cursor.rowcount > 0:
            # Fetch and return the updated data.
            select_query = f"SELECT * FROM users WHERE username = '{username}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            # If no rows were affected, return None to indicate no update occurred.
            return None
    except Exception as e:
        print(f"Error while retrieving users record(s): {e}", file=sys.stderr)
        return None
    finally:
        cursor.close()
        connection.close()


def get_user(user_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    select_query = f"SELECT * FROM users WHERE id = '{user_id}'"

    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
        
    except Exception as e:
        print(f"Error while retrieving users record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def login(username, password):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
        
    except Exception as e:
        print(f"Error while retrieving users record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def set_status(status):
    try:
        with db.get_database_connection() as connection:
            connection.autocommit = True
            with connection.cursor() as cursor:
                query = "UPDATE users SET active = %s"
                cursor.execute(query, (status,))  # Pass parameters as a tuple
                
                return cursor.rowcount
    except Exception as e:
        print(f"Error while updating users record(s): {e}")
        return None


def get_all_users():
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    select_query = f"SELECT * FROM users"
    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()

        if not result:
            return None
        else:
            return result
        
    except Exception as e:
        print(f"Error while retrieving users record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def update_user(user_id, username, password, firstname, lastname, email, phone, address):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE users SET username='{username}', password='{password}', firstname='{firstname}', lastname='{lastname}', email='{email}', phone='{phone}', address='{address}' WHERE id={user_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        # Check if any rows were affected by the update.
        if cursor.rowcount > 0:
            # Fetch and return the updated data.
            select_query = f"SELECT * FROM users WHERE id = '{user_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            # If no rows were affected, return None to indicate no update occurred.
            return None
    except Exception as e:
        print(f"Error while updating user record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_password(user_id, password):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE users SET password='{password}' WHERE id='{user_id}'"
    
    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM users WHERE id = '{user_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating users record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def update_profile(user_id, img_path):
    BUCKET_NAME = 'medibottian'

    FILE_NAME = img_path
    OBJECT_NAME = f'{user_id}.jpg'

    s3 = boto3.client('s3', 
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name='us-east-2')

def update_profile(user_id, img_path):

    FILE_NAME = img_path
    OBJECT_NAME = f'user_profile/{user_id}.jpg'

    # Check if user_id.jpg exists in the S3 bucket
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        print("File exists, deleting now...")
        s3.delete_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
    except Exception as e:
        print("No existing file, uploading now...")

    # Upload the image to S3 bucket
    s3.upload_file(FILE_NAME, BUCKET_NAME, OBJECT_NAME)

    # Return the URL of the image
    img_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{OBJECT_NAME}"
    return img_url


def get_profile_pic(user_id):

    OBJECT_NAME = f'user_profile/{user_id}.jpg'

    # Check if user_id.jpg exists in the S3 bucket
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        print("File exists, returning the URL...")
        img_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{OBJECT_NAME}"
        return img_url
    except Exception as e:
        print("No existing file.")
        return None


def delete_user(user_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM users WHERE id = '{user_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "User record deleted successfully."
    except Exception as e:
        print(f"Error while retrieving users record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

