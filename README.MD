Cinema API

API service for cinema management written on DRF
Installing using GitHub:

Install PostgresSQL and create db
```
    git clone https://github.com/nekropo1/py-cinema
    cd cinema-api
    python -m venv venv
```
Linux/macOS:
```
  source venv/bin/activate
  pip install -r requirements.txt
  export DB_HOST=<your db hostname>
  export DB_NAME=<your db name>
  export DB_USER=<your db user>
  export DB_PASSWORD=<your db password>
  export DB_SECRET_KEY=<your secret key>
```
Windows: 
```  
  venv\Scripts\activate
  pip install -r requirements.txt
  set POSTGRES_HOST=<your db hostname>
  set POSTGRES_DB=<your db name>
  set POSTGRES_USER=<your db user>
  set POSTGRES_PASSWORD=<your db password>
  set DB_SECRET_KEY=<your secret key>
  python manage.py migrate
  python manage.py runserver
```
Run with docker

Docker should be installed

docker-compose up --build

Getting access

    create user via localhost/api/user/register/
    get access token via localhost/api/user/token/

Features

    JWT authenticated
    Admin panel localhost/admin/
    Documentation is located at localhost/api/doc/swagger/
    Managing orders and tickets
    Creating movies with genres, actors
    Creating cinema halls
    Adding movie sessions
    Filtering movies and movie sessions
