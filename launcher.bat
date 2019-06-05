
:: Replace flask_ajax.py with the name of the python file containing the name of the
:: flask application to run. Note that the syntax will be different for
:: running on linux

:: Activate the virtual environment (for windows)
:: If no virtual environment created yet, run python -m venv <environment name> from admin powershell
::.\venv\Scripts\activate

:: Installs all the requirements
:: pip install --upgrade -r app/requirements.txt

set FLASK_APP=main.py
flask run