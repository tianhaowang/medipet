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


def create_doctor(username, password, firstname, lastname, email, phone, address, medical_license):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    insert_query = f"INSERT INTO doctor (username, password, firstname, lastname, email, phone, address, `medical_license`) VALUES ('{username}', '{password}', '{firstname}', '{lastname}', '{email}', '{phone}', '{address}', '{medical_license}')"

    try:
        cursor.execute(insert_query)
        connection.commit()
        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM doctor WHERE username = '{username}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while creating doctor record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def login(username, password):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    select_query = f"SELECT * FROM doctor WHERE username = '{username}' AND password = '{password}'"
    
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

def get_doctor(doctor_id=None):
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    select_query = f"SELECT * FROM doctor WHERE id = '{doctor_id}'"

    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving doctor record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def get_all_doctors():
    connection = db.get_database_connection()
    cursor = connection.cursor()
    
    select_query = f"SELECT * FROM doctor"
    try:
        if select_query:
            cursor.execute(select_query)
        result = cursor.fetchall()
        if not result:
            return None
        else:
            return result
    except Exception as e:
        print(f"Error while retrieving doctor record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def update_password(doctor_id, password):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE doctor SET password='{password}' WHERE id='{doctor_id}'"
    
    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM doctor WHERE id = '{doctor_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating doctor record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def update_doctor(doctor_id, username, password, firstname, lastname, email, phone, address, medical_license):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    update_query = f"UPDATE doctor SET username='{username}', password='{password}', firstname='{firstname}', lastname='{lastname}', email='{email}', phone='{phone}', address='{address}', `medical_license`='{medical_license}' WHERE id={doctor_id}"

    try:
        cursor.execute(update_query)
        connection.commit()

        if cursor.rowcount > 0:
            select_query = f"SELECT * FROM doctor WHERE id = '{doctor_id}'"
            cursor.execute(select_query)
            updated_data = cursor.fetchall()
            return updated_data
        else:
            return None
    except Exception as e:
        print(f"Error while updating doctor record: {e}")
        return None
    finally:
        cursor.close()
        connection.close()


def delete_doctor(doctor_id):
    connection = db.get_database_connection()
    cursor = connection.cursor()

    delete_query = f"DELETE FROM doctor WHERE id = '{doctor_id}'"

    try:
        cursor.execute(delete_query)
        connection.commit()
        return "Doctor record deleted successfully."
    except Exception as e:
        print(f"Error while deleting doctor record(s): {e}")
        return None
    finally:
        cursor.close()
        connection.close()

def update_doctor_pic(doctor_id, img_path):
    FILE_NAME = img_path
    OBJECT_NAME = f'doctor_profile/{doctor_id}.jpg'

    # Check if doctor_id.jpg exists in the S3 bucket
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

def get_doctor_pic(doctor_id):
    OBJECT_NAME = f'doctor_profile/{doctor_id}.jpg'
    
    # Check if doctor_id.jpg exists in the S3 bucket
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=OBJECT_NAME)
        print("File exists, returning the URL...")
        img_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{OBJECT_NAME}"
        return img_url
    except Exception as e:
        print("No existing file.")
        return None