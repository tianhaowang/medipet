import boto3
import database.connect_db as db
import os

# S3 credentials
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = 'medibottian'


s3 = boto3.client('s3', 
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                region_name='us-east-2')

from mysql.connector import pooling

def create_medicine(name, description, recommended_dosage, image):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    # Constructing the insert query using f-strings (not recommended for user-provided values)
    insert_query = f"""
    INSERT INTO medicine (name, description, recommended_dosage, image) 
    VALUES ('{name}', '{description}', '{recommended_dosage}', '{image}')
    """

    try:
        cursor.execute(insert_query)
        connection.commit()

        if cursor.rowcount > 0:
            medicine_id = cursor.lastrowid
            select_query = f"SELECT * FROM medicine WHERE id = {medicine_id}"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            print(updated_data)
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while creating medicine record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_medicine(medicine_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM medicine WHERE id = '{medicine_id}'"

    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving medicine record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_all_medicines():
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM medicine"
    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving medicine record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_medicine(medicine_id, name, description, recommended_dosage):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE medicine SET name='{name}', description='{description}', recommended_dosage='{recommended_dosage}' WHERE id={medicine_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM medicine WHERE id = '{medicine_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating medicine record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def delete_medicine(medicine_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM medicine WHERE id = '{medicine_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "Medicine record deleted successfully."
    except Exception as e:
        print(f"Error while deleting medicine record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def update_medicine_pic(medicine_id, img_path):
    FILE_NAME = img_path
    OBJECT_NAME = f'medicine/{medicine_id}.jpg'

    # Check if medicine_id.jpg exists in the S3 bucket
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

def get_medicine_pic(medicine_id):
    OBJECT_NAME = f'medicine/{medicine_id}.jpg'
    
    # Check if medicine_id.jpg exists in the S3 bucket
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        print("File exists, returning the URL...")
        img_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{OBJECT_NAME}"
        return img_url
    except Exception as e:
        print("No existing file.")
        return None