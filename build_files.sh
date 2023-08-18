cd ..
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py runserver
