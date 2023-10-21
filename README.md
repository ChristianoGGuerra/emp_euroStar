# emp_euroStar
Temporary website did in Django and PSQL

 ## Need to configure the django site application
 *** Step to do: Open the terminal and add ``` export DJANGO_SETTINGS_MODULE=euroemp.settings ``` also ``` set DJANGO_SETTINGS_MODULE=euroemp.settings ``` 
*** Those commands will be start django by our application, not the default that is mysite.settings.

## Need to configure the postgresql database
*** Step to do: ``` pyp3 install postgresql ``` or ``` brew install postgresql ``` then run ``` brew install libpq ``` and the last command is ``` brew link --force libpq ``` and configure the postgres database.

## Need to create user, database, and migrate all tables in the postgresql
*** Going to pgadmin or psql command and create an user, password and database, the name of database, user and the password is in the emp_euroStar folde, settings.py

*** Via pgadmin go to Login/Grupo Roles and create a new one --> Then go to Database and create a new db named eurostar

*** Via psql command in the terminal write ```psql ```, in the psql terminal write ``` CREATE USER eurostar WITH PASSWORD 'ourpass'; ``` and then ``` CREATE DATABASE name WITH OWNER = eurostar; ```

*** Exit the psql or in the terminal write ``` python3 manage.py migrate ```, then ``` python3 manage.py makemigration addr ``` for the others modules too, company and employee, so the migration file is create, now need to run the migration for each module ```python3 manage.py migrate addr ``` and the same for the other modules.

## Need start the project
*** In the same termina write ``` python3 manage.py runserver ```

## Need to populate the country table
*** Step to do: Open the terminal and apply the command ```python3 manage.py load_countries```

 - Have three modules
 - Until 21 of Sep only one is done (Employee Registration)
 - In Progress Company( A list of companies and total of employees in a table) and Address that has relation with Employee and Company
 - Each Employee is related to only one company

