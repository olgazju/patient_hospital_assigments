# Patient cost explorer

Create a new Django project.

Build a patient cost explorer. 
Create the models to store patients (first name, last name, age, id), hospitals (hospital id, name), treatments (treatment id, hospital id, treatment name, price) and treatments for patients (patient id, treatment id) in a local sqlite database.

Create a most basic UI (simple HTML form) to create entities for each of these categories.

## How to set enviroment on Windows:
 1. Install [Python 3.6 version](https://www.python.org/downloads/release/python-360/). 
Make sure that C:\Program Files (x86)\Python36-32; and C:\Program Files (x86)\Python36-32\Scripts; is part of your PATH.

 2. Install vitrualenv to create individual environment
 
`pip install virtualenv`

 3. Create enviroment:
 

`mkdir C:\virtualenv`

`cd C:\virtualenv`

`virtualenv cost_explorer`

 4. Activate enviroment
 
`cd C:\virtualenv\cost_explorer\Scripts`

`activate`

 5. Clone repository
 
 `cd C:\`

 `git clone https://github.com/olgazju/patient_hospital_assigments.git`

 6. Install requirements
 
`cd patient_hospital_assigments`

`pip install -r requirements.txt`

7. Run server

`cd patient_hospital_assigments`

`python manage.py runserver`

## How to run app:

Open http://127.0.0.1:8000
