-- 1. Levothyroxine
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Levothyroxine', 'Levothyroxine is a synthetic form of thyroxine (thyroid hormone) used to treat hypothyroidism (underactive thyroid). It helps restore the proper level of thyroid hormone in the body, contributing to regulating energy, metabolism, and overall physical and mental well-being.', 'The recommended starting dosage for adults with hypothyroidism is typically 1.6 micrograms per kilogram of body weight per day, taken orally on an empty stomach, ideally 30 minutes to one hour before breakfast. Dosage may vary based on age, weight, medical condition, and response to treatment. Consult with a healthcare provider for the correct dosage.', 's3://medibottian/medicine/Levothyroxine.jpeg');

-- 2. Amoxicillin
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Amoxicillin', 'Amoxicillin is a penicillin antibiotic that fights bacteria. It is used to treat many different types of infections caused by bacteria, such as tonsillitis, bronchitis, pneumonia, and infections of the ear, nose, throat, skin, or urinary tract.', 'The recommended dose for adults is 250-500 mg every 8 hours or 500-875 mg every 12 hours, depending on the severity and type of infection. For children, the dose varies based on body weight. Always follow the prescribed dosage by a healthcare provider.', 's3://medibottian/medicine/Amoxicillin.jpeg');

-- 3. Lisinopril
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Lisinopril', 'Lisinopril is an ACE inhibitor used to treat high blood pressure (hypertension) and congestive heart failure. It is also used to improve survival after a heart attack.', 'The typical starting dose for hypertension is 10 mg once a day, with maintenance doses ranging from 20 to 40 mg per day, depending on the patient’s response and condition. Consult a healthcare provider for the correct dosage.', 's3://medibottian/medicine/Lisinopril.jpeg');

-- 4. Metformin
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Metformin', 'Metformin is used to improve blood sugar control in people with type 2 diabetes. It is used in combination with a proper diet and exercise program.', 'The starting dose is usually 500 mg orally twice a day or 850 mg once a day, with meals to reduce gastrointestinal side effects. Dosage can be increased gradually based on blood sugar levels and tolerance, up to a maximum of 2000-2550 mg per day.', 's3://medibottian/medicine/Metformin.jpeg');

-- 5. Amlodipine
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Amlodipine', 'Amlodipine is a calcium channel blocker used to treat high blood pressure (hypertension) and chest pain (angina). It works by relaxing the blood vessels so that blood can flow more easily.', 'The usual initial antihypertensive oral dose of Amlodipine is 5 mg once daily, with a maximum dose of 10 mg daily. Adjustments should be made according to the patient’s response and tolerance.', 's3://medibottian/medicine/Amlodipine.jpeg');

-- 6. Simvastatin
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Simvastatin', 'Simvastatin is a statin medication used to control elevated cholesterol, or hyperlipidemia. It is also used to prevent cardiovascular disease.', 'The usual starting dose is 20 to 40 mg once a day in the evening. Dosage adjustments should be made based on the patient’s response and tolerance, not exceeding 40 mg per day.', 's3://medibottian/medicine/Simvastatin.jpeg');

-- 7. Albuterol
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Albuterol', 'Albuterol is a bronchodilator that relaxes muscles in the airways and increases air flow to the lungs. It is used to treat or prevent bronchospasm in people with reversible obstructive airway disease and to prevent exercise-induced bronchospasm.', 'The recommended dose for adults and children 4 years of age and older for the treatment of acute episodes of bronchospasm or prevention of asthmatic symptoms is two inhalations every 4 to 6 hours. For exercise-induced bronchospasm, the dose is two inhalations 15 to 30 minutes before exercise.', 's3://medibottian/medicine/Albuterol.jpeg');

-- 8. Ibuprofen
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Ibuprofen', 'Ibuprofen is a nonsteroidal anti-inflammatory drug (NSAID) used to reduce fever and treat pain or inflammation caused by many conditions such as headache, toothache, back pain, arthritis, menstrual cramps, or minor injury.', 'The typical dose for adults is 200 to 400 mg orally every 4 to 6 hours as needed. The maximum daily dose should not exceed 3200 mg.', 's3://medibottian/medicine/Ibuprofen.jpeg');

-- 9. Acetaminophen (Tylenol)
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Acetaminophen', 'Acetaminophen (Tylenol) is used to treat mild to moderate pain and to reduce fever. It is used for headaches, muscle aches, backaches, toothaches, colds, and fevers.', 'Adults and children 12 years and older can take 650 to 1000 mg every 4 to 6 hours as needed, not exceeding 3000 mg per day.', 's3://medibottian/medicine/Acetaminophen.jpeg');

-- 10. Hydrochlorothiazide
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Hydrochlorothiazide', 'Hydrochlorothiazide is a diuretic medication often used to treat high blood pressure and swelling due to fluid build up. It helps your body get rid of extra salt and water.', 'The typical dose is 25 to 50 mg once daily, often starting at the lower end of this range and adjusting according to the response and condition of the patient.', 's3://medibottian/medicine/Hydrochlorothiazide.jpeg');

-- 11. Cetirizine
INSERT INTO medicine (name, description, recommended_dosage, image) 
VALUES ('Cetirizine', 'Cetirizine is an antihistamine used to relieve allergy symptoms such as watery eyes, runny nose, itching eyes/nose, sneezing, hives, and itching. It works by blocking a certain natural substance (histamine) that your body makes during an allergic reaction.', 'The recommended dose for adults and children over 6 years of age is 10 mg once daily.', 's3://medibottian/medicine/Cetirizine.jpeg');

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/1a276106-7b0d-4daf-b806-559f89a6ae74_Acetaminophen' 
WHERE name = 'Acetaminophen';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/27514c6e-8e0c-4b26-b823-540fbdeb2f46_Lisinopril' 
WHERE name = 'Lisinopril';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/5d71a7fb-26f2-461c-b5c3-4f1439efdec5_Cetirizine' 
WHERE name = 'Cetirizine';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/85e19377-a276-426c-ba74-6153dcc38550_Ibuprofen' 
WHERE name = 'Ibuprofen';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/97bd0a8b-91fa-4c11-ad55-81944982df9d_Metformin' 
WHERE name = 'Metformin';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/97d4bd45-097d-4d9a-aa47-ecc9570906a5_Amoxicillin' 
WHERE name = 'Amoxicillin';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/a98f6296-6f02-4962-9aa7-dbdb680ecf1e_Albuterol' 
WHERE name = 'Albuterol';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/ae05469d-e081-43c3-b1c6-1c3456fcb88e_hydrochlorothiazide' 
WHERE name = 'Hydrochlorothiazide';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/cba1718e-9616-4fd6-8894-fbc34934ee2a_Amlodipine' 
WHERE name = 'Amlodipine';

UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/e2826411-428c-4500-aef3-6b161fa5e53f_Simvastatin' 
WHERE name = 'Simvastatin';

-- For Levothyroxine, if you have the correct link, replace 'your_correct_link_here' with the actual link
UPDATE medicine 
SET image = 'https://medibottian.s3.us-east-2.amazonaws.com/medicine/Levothyroxine.jpeg' 
WHERE name = 'Levothyroxine';
