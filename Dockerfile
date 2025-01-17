FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install django

RUN pip install pymysql

RUN pip install mysqlclient

RUN pip install Pillow

RUN pip install pyodbc 

RUN pip install django-environ

RUN pip install django-ses

RUN pip install pipenv && pipenv install

COPY . . 




CMD ["bash", "startup.sh", "prod"]
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]




