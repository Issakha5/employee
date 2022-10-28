# Employee Management
## clone the repository 
## Set up a virtual environment and activate them
python -m venv env && source env/bin/activate
## Install requirements.txt
pip install -r requirements.txt
## This part is optional Create Admin User
python manage.py createsuperuser
## Run the Server
python manage.py runserver
## Visit Urls
### CRUD APP
localhost:8000/  or 127.0.0.1:8000/

### API
localhost:8000/employee  or 127.0.0.1:8000/employee
