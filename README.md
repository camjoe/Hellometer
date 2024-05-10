# Hellometer
 
# Front end and back end project to showcase development background

# Setup Postgresql Database
- Must have postgresql downloaded
- Set databse.ini file with:
[postgresql]
host
database
user
password
- Set local directory for csv files in postgresql/settings.py
- Run create_tables to create table in postgresql database
- Run insert_data to insert csv data into table

# Run tests
In Command line from project folder,
- python -m unittest

# Run the server
From hellometer_dashboard run:
- python manage.py runserver
From dashboard run:
- npm start