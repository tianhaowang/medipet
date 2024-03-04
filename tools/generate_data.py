from faker import Faker
from database.doctor import create_doctor
from database.users import create_user
from database.conditions import create_condition  # Assuming you have a similar create_condition function
from database.medicine import create_medicine  # Assuming you have a similar create_medicine function

fake = Faker()

condition_list = ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Allergies", "Cancer", "COVID-19", "Arthritis", "Obesity", "Depression"]
medicine_list = ["Aspirin", "Ibuprofen", "Paracetamol", "Lisinopril", "Atorvastatin", "Metformin", "Amoxicillin", "Omeprazole"]

for _ in range(100):
    doctor_data = {
        'username': fake.unique.user_name(),
        'password': fake.password(),
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'email': fake.unique.email(),
        'phone': fake.phone_number(),
        'address': fake.address(),
        'medical_license': fake.unique.random_number(digits=10)  # Adjust this as necessary
    }
    create_doctor(**doctor_data)

    user_data = {
        'username': fake.unique.user_name(),
        'password': fake.password(),
        'firstname': fake.first_name(),
        'lastname': fake.last_name(),
        'email': fake.unique.email(),
        'phone': fake.phone_number(),
        'address': fake.address()
    }
    create_user(**user_data)   # Assuming you have a similar create_user function
    
    condition_data = {
        'name': fake.random_element(condition_list)
    }
    create_condition(**condition_data)   # Assuming you have a similar create_condition function
    
    medicine_data = {
        'name': fake.random_element(medicine_list),
        'description': fake.text(max_nb_chars=200),
        'recommended_dosage': fake.text(max_nb_chars=50)
    }
    create_medicine(**medicine_data)  # Assuming you have a similar create_medicine function
