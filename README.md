[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-382/)

# Blog

## How to start?
Your first commands would be:
```
git clone <SSH address of this repo>
cd blog/
python3 -m myenv venv
source venv\bin\activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py createsuperuser
python3 manage.py runserver
```
After starting Django, a link like http://127.0.0.1:8000/ will appear - click on it.

The app is ready for local use!