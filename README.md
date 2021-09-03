#### HUMAN BRAND - TECHNICAL TEST

### Terminal commands
Note: make sure you have `pip` and `virtualenv` installed.

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all

Make sure to run the initial migration commands to update the database.
    
    > python manage.py db init

    > python manage.py db migrate --message 'initial database migration'

    > python manage.py db upgrade


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/

### Convert a amount ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/currency?amount=5&option=3, change the amount by
    the value expected and the option between:
    1 = Euros a dólares 
    2 = Pesos chilenos a dólares
    3 = Soles a dólares 

### Get a amount ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/currency/amount_expected, change the amount by
    the value spected. In this request send body to WEBHOOK STABLISH.