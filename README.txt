========================== README ==========================

It's our project for the web site for online shop.
We've done it with django and SQLite for then backend, and html and css for the frontend

To run local host and go to site, change directory to project's main directory and enter this command to terminal:
Windows:
python manage.py runserver

MacOS/Linux:
python3 manage.py runserver

If u see error that that port is already used:
'Error: That port is already in use.'
add localhost:<any other port that u dont use> to command

for example:
Windows:
python manage.py runserver localhost:1234
or
python manage.py runserver 1234

MacOS/Linux:
python3 manage.py runserver localhost:1234
or
python3 manage.py runserver 1234

You can also see error shows, that django can't find a settings.py file. To fix that, go to Run -> edit configurations -> edit enviroment variables -> add DJANGO_SETTINGS_MODULE=pet_site.settings or other path to this file in this string

