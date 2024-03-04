from flask import Flask, request, jsonify
import database.users as db_user
from flask_cors import CORS, cross_origin
import database.doctor as db_doctor
import database.medicine as db_medicine
import database.conditions as db_condition
import database.doctor_user as db_du
import database.user_conditions as db_uc
import database.schedule as db_schedule
import database.children as db_children
import aws.storage as storage
from werkzeug.utils import secure_filename
import datetime
import sys
storage.configure_aws_credentials()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
cors = CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*", "allow_headers": "*"}})
app.config['CORS_HEADERS'] = '*'

def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase characters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check if the password contains at least one special character
    special_characters = "!@#$%^&*()-_=+[]{};:'\",<.>/?\|`~"
    if not any(char in special_characters for char in password):
        return False

    # If all checks pass
    return True

# Endpoint for creating a child
@app.route('/children', methods=['POST'])
@cross_origin()
def create_child_endpoint():
    data = request.get_json()
    # Removed child_uname, child_number, and parent_number as they are not part of the updated create_child function
    parent_id = data.get('Parent_id')
    points = data.get('Points')
    hunger = data.get('Hunger')
    happiness = data.get('Happiness')
    health = data.get('Health')
    alert_threshold = data.get('Alert_threshold')
    miss_threshold = data.get('Miss_threshold')

    # You may want to add your own validation logic here

    # Updated to match the parameters of the updated create_child function
    result = db_children.create_child(parent_id, points, hunger, happiness, health, alert_threshold, miss_threshold)
    if result is not None:
        # Map the response data correctly based on the database insert result
        response_data = {key: value for key, value in zip(['id', 'Parent_id', 'Points', 'Hunger', 'Happiness', 'Health', 'Alert_threshold', 'Miss_threshold'], result)}
        return jsonify(response_data), 201
    else:
        # If child creation failed, return a JSON response with an error message
        error_message = {"error": "Child creation failed."}
        return jsonify(error_message), 400


# Endpoint for retrieving child data by username
@app.route('/children/<username>', methods=['GET'])
@cross_origin()
def get_child_data_endpoint(username):
    result = db_children.get_child_data_by_username(username)
    if result is not None and len(result) > 0:
        # If the child data was found, map the response data correctly
        response_data = {key: value for key, value in zip(['id', 'Child_uname', 'Child_number', 'Parent_number', 'Parent_id', 'Points', 'Hunger', 'Happiness', 'Health', 'Alert_threshold', 'Miss_threshold'], result[0])}
        return jsonify(response_data), 200
    else:
        # If no data was found for the child, return a JSON response with an error message
        error_message = {"error": f"No data found for child with username {username}."}
        return jsonify(error_message), 404  # Changed to 404 which is more appropriate for not found

    
# Endpoint for updating a child
@app.route('/children/<int:id>', methods=['POST'])
@cross_origin()
def update_child_endpoint(id):
    data = request.get_json()

    # Extract data for all fields that might be updated
    child_uname = data.get('Child_uname')
    child_number = data.get('Child_number')
    parent_number = data.get('Parent_number')
    parent_id = data.get('Parent_id')
    points = data.get('Points')
    hunger = data.get('Hunger')
    happiness = data.get('Happiness')
    health = data.get('Health')
    alert_threshold = data.get('Alert_threshold')
    miss_threshold = data.get('Miss_threshold')

    # Call the database function to update the child
    result = db_children.update_child(id, child_uname, child_number, parent_number, parent_id, points, hunger, happiness, health, alert_threshold, miss_threshold)
    
    if result:
        # If the child was updated successfully, return a success response
        return jsonify({"message": "Child updated successfully."}), 200
    else:
        # If child update failed, return a JSON response with an error message
        error_message = {
            "error": "Child update failed."
        }
        return jsonify(error_message), 400
    
# USERS
@app.route('/users', methods=['POST'])
@cross_origin()
def create_user_endpoint():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    if not validate_password(password):
        error_message = {
            "error": "Password Invalid. Minimum 8 length, Upper case Lowercase, numbers and at least 1 symbol must be used"
        }
        return jsonify(error_message), 400   
    
    result = db_user.create_user(username, password, firstname, lastname, email, phone, address)
    if result is not None:
        # If the user was created successfully, return a JSON response
        user_id, username, password, firstname, lastname, email, phone, address, status = result[0]

        response_data = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "status" : status
        }

        return jsonify(response_data), 201
    else:
        # If user creation failed, return a JSON response with an error message
        error_message = {
            "error": "User creation failed."
        }

        return jsonify(error_message), 400   

@app.route('/users/password', methods=['PUT'])
@cross_origin()
def update_user_password():
    data = request.get_json()
    user_id = data.get('id')
    password = data.get('password')

    if not validate_password(password):
        error_message = {
            "error": "Password Invalid. Minimum 8 length, Upper case Lowercase, numbers and at least 1 symbol must be used"
        }
        return jsonify(error_message), 400
    
    result = db_user.update_password(user_id, password)

    if result is not None:
        response_data = {
            "message" : "success"
        }
        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Password Update failed"
        }

        return jsonify(error_message), 400  
        


@app.route('/users', methods=['PATCH'])
@cross_origin()
def get_user_endpoint():
    data = request.get_json()
    id = data.get('id')

    result = db_user.get_user(id)

    if result is not None:

        # If the user was created successfully, return a JSON response
        user_id, username, password, firstname, lastname, email, phone, address, status = result[0]

        response_data = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "status": status
        }

        return jsonify(response_data), 200
    else:
        # If user creation failed, return a JSON response with an error message
        error_message = {
            "error": "User creation failed."
        }

        return jsonify(error_message), 400   

@app.route('/users/login', methods=['POST'])
@cross_origin()
def user_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    result = db_user.login(username, password)

    if result is not None:

        # If the user was created successfully, return a JSON response
        user_id, username, password, firstname, lastname, email, phone, address, status = result[0]

        response_data = {
            "user_id": user_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address
        }

        return jsonify(response_data), 200
    else:
        # If user creation failed, return a JSON response with an error message
        error_message = {
            "error": "User Login failed."
        }

        return jsonify(error_message), 400   
    
@app.route('/users/set_status', methods=['POST'])
@cross_origin()
def set_user_status():
    data = request.get_json()
    status = data.get('status')

    result = db_user.set_status(status=status)

    if result is not None:
        response_data = {
            "message":"updated"
        }

        return jsonify(response_data), 200
    else:
        # If user creation failed, return a JSON response with an error message
        error_message = {
            "error": "Failed to update"
        }

        return jsonify(error_message), 400   

@app.route('/users/logout', methods=['POST'])
@cross_origin()
def user_logout():

    response_data = {
        "message":"logout"
    }

    return jsonify(response_data), 200
    
# Update a user
@app.route('/users', methods=['PUT'])
@cross_origin()
def update_user_endpoint():
    data = request.get_json()
    user_id = data.get('id')
    username = data.get('username')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')

    result = db_user.update_user(user_id, username, password, firstname, lastname, email, phone, address)
    
    if result is not None:
        # If the user was updated successfully, return a JSON response
        user_id, username, password, firstname, lastname, email, phone, address, active = result[0]

        response_data = {
            "user_id": user_id,
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address
        }

        return jsonify(response_data), 200
    else:
        # If user update failed, return a JSON response with an error message
        error_message = {
            "error": "User update failed."
        }

        return jsonify(error_message), 400   

# Delete a user
@app.route('/users', methods=['DELETE'])
@cross_origin()
def delete_user_endpoint():
    data = request.get_json()
    user_id = data.get('id')

    result = db_user.delete_user(user_id)

    if result is not None:
        # If the user was deleted successfully, return a JSON response
        response_data = {
            "message": "User record deleted successfully."
        }

        return jsonify(response_data), 200
    else:
        # If user deletion failed, return a JSON response with an error message
        error_message = {
            "error": "User deletion failed."
        }

        return jsonify(error_message), 400   

@app.route('/users/all', methods=['PATCH'])
@cross_origin()
def get_all_users_endpoint():
    result = db_user.get_all_users()
    if result is not None:
        # If the operation was successful, return a JSON response with all users
        response_data = []
        for row in result:
            user_id, username, password, firstname, lastname, email, phone, address, status = row
            response_data.append({
                "user_id": user_id,
                "username": username,
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "phone": phone,
                "address": address,
                "status": status
            })

        return jsonify(response_data), 200
    else:
        # If operation failed, return a JSON response with an error message
        error_message = {
            "error": "Failed to fetch all users."
        }

        return jsonify(error_message), 400   

# Doctor Endpoints

@app.route('/doctors', methods=['POST'])
@cross_origin()
def create_doctor_endpoint():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')
    medical_license = data.get('medical_license')

    if not validate_password(password):
        error_message = {
            "error": "Password Invalid. Minimum 8 length, Upper case Lowercase, numbers and at least 1 symbol must be used"
        }
        return jsonify(error_message), 400
    
    result = db_doctor.create_doctor(username, password, firstname, lastname, email, phone, address, medical_license)
    if result is not None:
        doctor_id, username, password, firstname, lastname, email, phone, address, medical_license = result[0]
        response_data = {
            "doctor_id": doctor_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "medical_license": medical_license
        }

        return jsonify(response_data), 201

    else:
        error_message = {
            "error": "Doctor creation failed."
        }

        return jsonify(error_message), 400  

@app.route('/doctors/login', methods=['POST'])
@cross_origin()
def doctor_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    result = db_doctor.login(username, password)

    if result is not None:

        # If the user was created successfully, return a JSON response
        doctor_id, username, password, firstname, lastname, email, phone, address, medical_license = result[0]

        response_data = {
            "doctor_id": doctor_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "medical_license":medical_license
        }

        return jsonify(response_data), 200
    else:
        # If user creation failed, return a JSON response with an error message
        error_message = {
            "error": "Doctor login failed."
        }

        return jsonify(error_message), 400 
    
@app.route('/doctors/logout', methods=['POST'])
@cross_origin()
def doctor_logout():

    response_data = {
        "message":"logout"
    }

    return jsonify(response_data), 200

@app.route('/doctors', methods=['PATCH'])
@cross_origin()
def get_doctor_endpoint():
    data = request.get_json()
    id = data.get('id')

    result = db_doctor.get_doctor(id)

    if result is not None:
        doctor_id, username, password, firstname, lastname, email, phone, address, medical_license = result[0]
        response_data = {
            "doctor_id": doctor_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "medical_license": medical_license
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor retrieval failed."
        }

        return jsonify(error_message), 400  

@app.route('/doctors/password', methods=['PUT'])
@cross_origin()
def update_doctor_password():
    data = request.get_json()
    doctor_id = data.get('id')
    password = data.get('password')

    if not validate_password(password):
        error_message = {
            "error": "Password Invalid. Minimum 8 length, Upper case Lowercase, numbers and at least 1 symbol must be used"
        }
        return jsonify(error_message), 400
    
    result = db_doctor.update_password(doctor_id, password)

    if result is not None:
        response_data = {
            "message" : "success"
        }
        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Password Update failed"
        }

        return jsonify(error_message), 400  
        

@app.route('/doctors', methods=['PUT'])
@cross_origin()
def update_doctor_endpoint():
    data = request.get_json()
    doctor_id = data.get('id')
    username = data.get('username')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    email = data.get('email')
    phone = data.get('phone')
    address = data.get('address')
    medical_license = data.get('medical_license')

    result = db_doctor.update_doctor(doctor_id, username, password, firstname, lastname, email, phone, address, medical_license)

    if result is not None:
        doctor_id, username, password, firstname, lastname, email, phone, address, medical_license = result[0]
        response_data = {
            "doctor_id": doctor_id,
            "username": username,
            "password": password,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "medical_license": medical_license
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor update failed."
        }

        return jsonify(error_message), 400  

@app.route('/doctors', methods=['DELETE'])
@cross_origin()
def delete_doctor_endpoint():
    data = request.get_json()
    doctor_id = data.get('id')

    result = db_doctor.delete_doctor(doctor_id)

    if result is not None:
        response_data = {
            "message": "Doctor record deleted successfully."
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor deletion failed."
        }

        return jsonify(error_message), 400  

@app.route('/doctors/all', methods=['PATCH'])
@cross_origin()
def get_all_doctors_endpoint():
    result = db_doctor.get_all_doctors()

    if result is not None:
        response_data = []
        for row in result:
            doctor_id, username, password, firstname, lastname, email, phone, address, medical_license = row
            response_data.append({
                "doctor_id": doctor_id,
                "username": username,
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "phone": phone,
                "address": address,
                "medical_license": medical_license
            })

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Failed to fetch all doctors."
        }

        return jsonify(error_message), 400  
    

# Medicine Endpoints
@app.route('/medicines', methods=['POST'])
@cross_origin()
def create_medicine_endpoint():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    recommended_dosage = data.get('recommended_dosage')
    
    result = db_medicine.create_medicine(name, description, recommended_dosage)
    if result is not None:
        medicine_id, name, description, recommended_dosage = result[0]
        response_data = {
            "medicine_id": medicine_id,
            "name": name,
            "description": description,
            "recommended_dosage": recommended_dosage,
            "image": ""
        }

        return jsonify(response_data), 201

    else:
        error_message = {
            "error": "Medicine creation failed."
        }

        return jsonify(error_message), 400  

@app.route('/medicines_with_image', methods=['POST'])
@cross_origin()
def create_medicine_with_image_endpoint():
    # Check if the post request has the file part
    if   'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # You might want to add a unique identifier or timestamp to filename before saving
        # to avoid overwriting existing files with the same name

        # Now process the other form data
        data = request.form
        name = data.get('name')
        description = data.get('description')
        recommended_dosage = ""

        # Upload the file to AWS S3
        # Adjust the following line according to your storage.upload_request_to_s3 function requirements
        file_url = storage.upload_request_to_s3(file, filename, "medicine")
        
        if not file_url:
            error_message = {
                "error": "Could not upload image"
            }
            return jsonify(error_message), 400

        # Continue with creating the medicine record
        result = db_medicine.create_medicine(name, description, recommended_dosage, file_url)

        if result is not None:
            medicine_id, name, description, recommended_dosage, image = result[0]
            response_data = {
                "medicine_id": medicine_id,
                "name": name,
                "description": description,
                "recommended_dosage": recommended_dosage,
                "image_url": image 
            }
            return jsonify(response_data), 201
        else:
            error_message = {
                "error": "Medicine creation failed."
            }
            return jsonify(error_message), 400
    else:
        return jsonify({"error": "File type not allowed"}), 400
    
@app.route('/medicines', methods=['PATCH'])
@cross_origin()
def get_medicine_endpoint():
    data = request.get_json()
    medicine_id = data.get('id')

    result = db_medicine.get_medicine(medicine_id)

    if result is not None:
        medicine_id, name, description, recommended_dosage, image = result[0]
        response_data = {
            "medicine_id": medicine_id,
            "name": name,
            "description": description,
            "recommended_dosage": recommended_dosage,
            "image" : image
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Medicine retrieval failed."
        }

        return jsonify(error_message), 400  

@app.route('/medicines', methods=['PUT'])
@cross_origin()
def update_medicine_endpoint():
    data = request.get_json()
    medicine_id = data.get('id')
    name = data.get('name')
    description = data.get('description')
    recommended_dosage = ""

    result = db_medicine.update_medicine(medicine_id, name, description, recommended_dosage)


    if result is not None:
        medicine_id, name, description, recommended_dosage, image = result[0]
        response_data = {
            "medicine_id": medicine_id,
            "name": name,
            "description": description,
            "recommended_dosage": recommended_dosage,
            "image": image
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Medicine update failed."
        }

        return jsonify(error_message), 400  

@app.route('/medicines', methods=['DELETE'])
@cross_origin()
def delete_medicine_endpoint():
    data = request.get_json()
    medicine_id = data.get('id')

    # First, retrieve the medicine record to get the image URL
    result = db_medicine.get_medicine(medicine_id)
    if result is None:
        return jsonify({"error": "Medicine not found."}), 404

    # Extract the image URL from the medicine record
    medicine_id, name, description, recommended_dosage, image = result[0]

    # Delete the image from S3
    if image:
        delete_success = storage.delete_object_from_s3_by_url(image)
        if not delete_success:
            return jsonify({"error": "Failed to delete associated image from storage."}), 500

    # Proceed to delete the medicine record from the database
    result = db_medicine.delete_medicine(medicine_id)
    if result:
        response_data = {
            "message": "Medicine record deleted successfully."
        }
        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Medicine deletion failed."
        }
        return jsonify(error_message), 400
    
@app.route('/medicines/all', methods=['PATCH'])
@cross_origin()
def get_all_medicines_endpoint():
    result = db_medicine.get_all_medicines()

    if result is not None:
        response_data = []
        for row in result:
            medicine_id, name, description, recommended_dosage, image = row
            response_data.append({
                "medicine_id": medicine_id,
                "name": name,
                "description": description,
                "recommended_dosage": recommended_dosage,
                "image": image
            })

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Failed to fetch all medicines."
        }

        return jsonify(error_message), 400  
    
# Condition endpoints
@app.route('/conditions', methods=['POST'])
@cross_origin()
def create_condition_endpoint():
    data = request.get_json()
    name = data.get('name')

    result = db_condition.create_condition(name)
    if result is not None:
        condition_id, name = result[0]
        response_data = {
            "condition_id": condition_id,
            "name": name
        }

        return jsonify(response_data), 201

    else:
        error_message = {
            "error": "Condition creation failed."
        }

        return jsonify(error_message), 400  


@app.route('/conditions', methods=['PATCH'])
@cross_origin()
def get_condition_endpoint():
    data = request.get_json()
    condition_id = data.get('id')

    result = db_condition.get_condition(condition_id)

    if result is not None:
        condition_id, name = result[0]
        response_data = {
            "condition_id": condition_id,
            "name": name
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Condition retrieval failed."
        }

        return jsonify(error_message), 400  


@app.route('/conditions', methods=['PUT'])
@cross_origin()
def update_condition_endpoint():
    data = request.get_json()
    condition_id = data.get('id')
    name = data.get('name')

    result = db_condition.update_condition(condition_id, name)

    if result is not None:
        condition_id, name = result[0]
        response_data = {
            "condition_id": condition_id,
            "name": name
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Condition update failed."
        }

        return jsonify(error_message), 400  


@app.route('/conditions', methods=['DELETE'])
@cross_origin()
def delete_condition_endpoint():
    data = request.get_json()
    condition_id = data.get('id')

    result = db_condition.delete_condition(condition_id)

    if result is not None:
        response_data = {
            "message": "Condition record deleted successfully."
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Condition deletion failed."
        }

        return jsonify(error_message), 400  


@app.route('/conditions/all', methods=['PATCH'])
@cross_origin()
def get_all_conditions_endpoint():
    result = db_condition.get_all_conditions()

    if result is not None:
        response_data = []
        for row in result:
            condition_id, name = row
            response_data.append({
                "condition_id": condition_id,
                "name": name
            })

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Failed to fetch all conditions."
        }

        return jsonify(error_message), 400

# Doctor_user

# Doctor-User endpoints
@app.route('/doctor_user', methods=['POST'])
@cross_origin()
def create_doctor_user_endpoint():
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    user_id = data.get('user_id')

    result = db_du.create_doctor_user(doctor_id, user_id)
    if result is not None:
        response_data = {
            "id": result[0][0],
            "doctor_id": doctor_id,
            "user_id": user_id
        }

        return jsonify(response_data), 201

    else:
        error_message = {
            "error": "Doctor-user association creation failed."
        }

        return jsonify(error_message), 400 


@app.route('/doctor_user/doctor', methods=['PATCH'])
@cross_origin()
def get_doctor_by_user_endpoint():
    data = request.get_json()
    user_id = data.get('user_id')

    result = db_du.get_doctor_by_user(user_id)

    if result is not None:
        response_data = {
            "doctors": result
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor retrieval by user ID failed.",
            "doctors" : []
        }

        return jsonify(error_message), 404 


@app.route('/doctor_user/user', methods=['PATCH'])
@cross_origin()
def get_users_by_doctor_endpoint():
    data = request.get_json()
    doctor_id = data.get('doctor_id')

    result = db_du.get_users_by_doctor(doctor_id)

    if result is None:
        response_data = {
            "users": []
        }
        return jsonify(response_data), 200
    else:
        response_data = {
            "users": result
        }
        return jsonify(response_data), 200

@app.route('/doctor_user/doctor', methods=['PUT'])
@cross_origin()
def update_doctor_in_doctor_user_endpoint():
    data = request.get_json()
    doctor_user_id = data.get('id')
    new_doctor_id = data.get('doctor_id')

    result = db_du.update_doctor_in_doctor_user(doctor_user_id, new_doctor_id)

    if result is not None:
        response_data = {
            "id": result[0][0],
            "doctor_id": new_doctor_id,
            "user_id": result[0][2]
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor update in doctor-user association failed."
        }

        return jsonify(error_message), 400 


@app.route('/doctor_user/user', methods=['PUT'])
@cross_origin()
def update_user_in_doctor_user_endpoint():
    data = request.get_json()
    doctor_user_id = data.get('id')
    new_user_id = data.get('user_id')

    result = db_du.update_user_in_doctor_user(doctor_user_id, new_user_id)

    if result is not None:
        response_data = {
            "id": result[0][0],
            "doctor_id": result[0][1],
            "user_id": new_user_id
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "User update in doctor-user association failed."
        }

        return jsonify(error_message), 400 


@app.route('/doctor_user', methods=['DELETE'])
@cross_origin()
def delete_doctor_user_endpoint():
    data = request.get_json()
    doctor_user_id = data.get('id')

    result = db_du.delete_doctor_user(doctor_user_id)

    if result is not None:
        response_data = {
            "message": "Doctor-user association deleted successfully."
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor-user association deletion failed."
        }

        return jsonify(error_message), 400
    
@app.route('/doctor_id_user_id', methods=['DELETE'])
@cross_origin()
def delete_doctor_relation():
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    user_id = data.get('user_id')


    result = db_du.delete_relation(doctor_id,user_id)

    if result is not None:
        response_data = {
            "message": "Doctor-user association deleted successfully."
        }

        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Doctor-user association deletion failed."
        }

        return jsonify(error_message), 400

# User_Condition endpoints

@app.route('/user_condition', methods=['POST'])
@cross_origin()
def create_user_condition_endpoint():
    data = request.get_json()
    condition_id = data.get('condition_id')
    user_id = data.get('user_id')

    result = db_uc.create_user_condition(condition_id, user_id)

    if result is not None:
        response_data = {
            "id": result[0][0],
            "condition_id": condition_id,
            "user_id": user_id
        }

        return jsonify(response_data), 201

    else:
        error_message = {
            "error": "User-condition association creation failed."
        }

        return jsonify(error_message), 400 


@app.route('/user_condition/user', methods=['PATCH'])
@cross_origin()
def get_condition_by_user_endpoint():
    data = request.get_json()

    user_id = data.get('user_id')
    result = db_uc.get_condition_by_user(user_id)
    
    if result is not None:
        response_data = {
            "conditions": result
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Condition retrieval by user ID failed."
        }

        return jsonify(error_message), 400 


@app.route('/user_condition/condition', methods=['PATCH'])
@cross_origin()
def get_users_by_condition_endpoint():
    data = request.get_json()
    condition_id = data.get('condition_id')

    result = db_uc.get_users_by_condition(condition_id)

    if result is not None:
        response_data = {
            "users": result
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "User retrieval by condition ID failed."
        }

        return jsonify(error_message), 400 


@app.route('/user_condition/condition', methods=['PUT'])
@cross_origin()
def update_condition_in_user_condition_endpoint():
    data = request.get_json()
    user_condition_id = data.get('id')
    new_condition_id = data.get('condition_id')

    result = db_uc.update_condition_in_user_condition(user_condition_id, new_condition_id)

    if result is not None:
        response_data = {
            "id": result[0][0],
            "condition_id": new_condition_id,
            "user_id": result[0][2]
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Condition update in user-condition association failed."
        }

        return jsonify(error_message), 400 


@app.route('/user_condition/user', methods=['PUT'])
@cross_origin()
def update_user_in_user_condition_endpoint():
    data = request.get_json()
    user_condition_id = data.get('id')
    new_user_id = data.get('user_id')

    result = db_uc.update_user_in_user_condition(user_condition_id, new_user_id)

    if result is not None:
        response_data = {
            "id": result[0][0],
            "condition_id": result[0][1],
            "user_id": new_user_id
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "User update in user-condition association failed."
        }

        return jsonify(error_message), 400 


@app.route('/user_condition', methods=['DELETE'])
@cross_origin()
def delete_user_condition_endpoint():
    data = request.get_json()
    user_condition_id = data.get('id')

    result = db_uc.delete_user_condition(user_condition_id)

    if result is not None:
        response_data = {
            "message": "User-condition association deleted successfully."
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "User-condition association deletion failed."
        }

        return jsonify(error_message), 400

# Schedule endpoint

@app.route('/schedule/<int:schedule_id>', methods=['PUT'])
@cross_origin()
def update_taken_status(schedule_id):
    data = request.get_json()
    taken = data.get('taken')  # Assuming 'taken' is a boolean or similar value

    # Assuming db_schedule has a method to update the 'taken' status of a schedule
    result = db_schedule.update_taken_in_schedule(schedule_id, taken)

    if result:
        response_data = {
            "id": schedule_id,
            "taken": taken
        }
        return jsonify(response_data), 200
    else:
        error_message = {
            "error": "Schedule update failed."
        }
        return jsonify(error_message), 400
    
@app.route('/schedule', methods=['POST'])
@cross_origin()
def create_schedule_endpoint():
    data = request.get_json()
    user_id = data.get('user_id')
    medicine_id = data.get('medicine_id')
    time = data.get('time')
    taken = 0
    dosage = data.get('dosage')

    result = db_schedule.create_schedule(user_id, medicine_id, time, taken, dosage)

    if result is not None:
        response_data = {
            "id": result[0][0],
            "user_id": user_id,
            "medicine_id": medicine_id,
            "time": time,
            "taken": taken,
            "dosage": dosage
        }

        return jsonify(response_data), 201

    else:
        error_message = {
            "error": "Schedule creation failed."
        }

        return jsonify(error_message), 400 


@app.route('/schedule', methods=['PUT'])
@cross_origin()
def update_taken_in_schedule_endpoint():
    data = request.get_json()
    schedule_id = data.get('id')
    taken = data.get('taken')
    dosage = data.get('dosage')

    result = db_schedule.update_taken_in_schedule(schedule_id, taken)

    if result is not None:
        response_data = {
            "id": schedule_id,
            "user_id": result[0][1],
            "medicine_id": result[0][2],
            "time": result[0][3],
            "taken": taken,
            "dosage": dosage
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Schedule update failed."
        }

        return jsonify(error_message), 400 


@app.route('/schedule', methods=['PATCH'])
@cross_origin()
def get_schedule_endpoint():
    data = request.get_json()
    user_id = data.get('user_id')

    result = db_schedule.get_schedule(user_id)

    if result is not None:
        response_list = []
        for res in result:
            response_data = {
                "id": res[0],
                "user_id": res[1],
                "medicine_id": res[2],
                "time": res[3],
                "taken": res[4],
                "dosage": res[5]
            }
            response_list.append(response_data)
        return jsonify(response_list), 200
    if result is None:
        response_list = []
        return jsonify(response_list), 200
    else:
        error_message = {
            "error": "Schedule retrieval failed."
        }

        return jsonify(error_message), 400 


@app.route('/schedule', methods=['DELETE'])
@cross_origin()
def delete_schedule_endpoint():
    data = request.get_json()
    schedule_id = data.get('id')

    result = db_schedule.delete_schedule(schedule_id)

    if result is not None:
        response_data = {
            "message": "Schedule deleted successfully."
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Schedule deletion failed."
        }

        return jsonify(error_message), 400

# Profile picture endpoints
@app.route('/update_profile', methods=['POST'])
@cross_origin()
def update_profile_endpoint():
    data = request.get_json()
    user_id = data.get('user_id')
    img_path = data.get('img_path')

    img_url = db_user.update_profile(user_id, img_path)

    if img_url is not None:
        response_data = {
            "message": "Profile updated successfully.",
            "img_url": img_url
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Profile update failed."
        }

        return jsonify(error_message), 400

@app.route('/get_profile_pic', methods=['GET'])
@cross_origin()
def get_profile_pic_endpoint():
    data = request.get_json()
    user_id = data.get('user_id')

    img_url = db_user.get_profile_pic(user_id)

    if img_url is not None:
        response_data = {
            "message": "Profile picture retrieved successfully.",
            "img_url": img_url
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "No profile picture found."
        }

        return jsonify(error_message), 404

# Medicine pfp endpoints
@app.route('/update_medicine', methods=['POST'])
@cross_origin()
def update_medicine_pic_endpoint():
    data = request.get_json()
    medicine_id = data.get('medicine_id')
    img_path = data.get('img_path')

    img_url = db_medicine.update_medicine(medicine_id, img_path)

    if img_url is not None:
        response_data = {
            "message": "Medicine updated successfully.",
            "img_url": img_url
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Medicine update failed."
        }

        return jsonify(error_message), 400

@app.route('/get_medicine_pic', methods=['GET'])
@cross_origin()
def get_medicine_pic_endpoint():
    data = request.get_json()
    medicine_id = data.get('medicine_id')

    img_url =  db_medicine.get_medicine_pic(medicine_id)

    if img_url is not None:
        response_data = {
            "message": "Medicine picture retrieved successfully.",
            "img_url": img_url
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "No medicine picture found."
        }

        return jsonify(error_message), 404

@app.route('/update_doctor', methods=['POST'])
@cross_origin()
def update_doctor_pic_endpoint():
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    img_path = data.get('img_path')

    img_url = db_doctor.update_doctor_pic(doctor_id, img_path)

    if img_url is not None:
        response_data = {
            "message": "Doctor updated successfully.",
            "img_url": img_url
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "Doctor update failed."
        }

        return jsonify(error_message), 400

@app.route('/get_doctor_pic', methods=['GET'])
@cross_origin()
def get_doctor_pic_endpoint():
    data = request.get_json()
    doctor_id = data.get('doctor_id')

    img_url = db_doctor.get_doctor_pic(doctor_id)

    if img_url is not None:
        response_data = {
            "message": "Doctor picture retrieved successfully.",
            "img_url": img_url
        }

        return jsonify(response_data), 200

    else:
        error_message = {
            "error": "No doctor picture found."
        }

        return jsonify(error_message), 404
      
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
