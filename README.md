# emp_euroStar
Temporary website did in Django and PSQL

 ## Need to configure the django site application
 *** Step to do: Open the terminal and add ```export DJANGO_SETTINGS_MODULE=euroemp.settings``` also ```set DJANGO_SETTINGS_MODULE=euroemp.settings``` ***
Those commands will be start django by our application, not the default that is mysite.settings.

## Need to configure the postgresql database
*** Step to do: ```pyp3 install postgresql``` then set the user and password with the same values that are in euroemp/settings.py on DATABASES area.

## Need to populate the country table
*** Step to do: Open the terminal and apply the command ```django-admin run load_countries.py```

 - Have three modules
 - Until 21 of Sep only one is done (Employee Registration)
 - In Progress Company( A list of companies and total of employees in a table) and Address that has relation with Employee and Company
 - Each Employee is related to only one company

