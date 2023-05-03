Cinema API

API service for cinema management written on DRF

Installing using GitHub:

Install PostgresSQL and create db
```
    git clone https://github.com/nekropo1/py-cinema
    cd cinema-api
    python -m venv venv
```
Create a new .env file by copying .env.sample with
`cp .env.sample .env` on Linux or simply copypaste on Windows.

Open the .env file in a text editor and update the values
of the environment variables according to sample.

Linux/macOS:

```
  source venv/bin/activate
  pip install -r requirements.txt
  source .env
```
Windows: 
```  
  venv\Scripts\activate
  pip install -r requirements.txt
  npm install -g dotenv
```  
Change directory to your project, like in this sample:
`cd C:\myproject`
You should be able to run .env with simple `dotenv` command.

After these commands, on any system, run and apply migrations:
```
  python manage.py migrate
  python manage.py runserver
```

Run with docker:

Docker should be installed.

`docker-compose up --build`

Getting access:

    create user via localhost/api/user/register/
    get access token via localhost/api/user/token/

Features:

    JWT authenticated
    Admin panel localhost/admin/
    Documentation is located at localhost/api/doc/swagger/
    Managing orders and tickets
    Creating movies with genres, actors
    Creating cinema halls
    Adding movie sessions
    Filtering movies and movie sessions
