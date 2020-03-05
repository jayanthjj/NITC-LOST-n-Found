
# NITC LOST-n-Found

  

## Structure

  

The backend and frontend is in the same project. The frontend is in the highest directory and backend is in the `backend` directory.

  

## Backend

  

The backend folder contains the backend server. First install all the requirements.

```
pip install -r backend/requirements.txt
```

  

After installing reqirements change the MySQL credentials in the `backend/index.py` file. Replace the line 10 in the file with the credentisals of MySQL (username, password, database etc.).

  > **NOTE:** MySQL database is needed to run the server. Install it first and create a user with create and modify permissions for a database. 
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://**username**:**password**@localhost/**database**'
```
Initialize the MySQL database, this is only needed if you are running the server for the first time.
```
python 
from index import db
db.create_all()
```
This will create all the tables needed for the system. Then run the server to start the website, the default port for the server is `5000`.

```
python backend/main.py
```


## Frontend

Place the directory inside any web server folder and the entry point is `index.html`.