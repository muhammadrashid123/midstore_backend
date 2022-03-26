# midstore_backend
midstore backend API's


# Pre-requisites

Make sure to have installed the following pre-requisites for a development setup

1. Python 3.8 or greater
2. Install Postgresql database server.
3. Create a user by the name `admin` and password `admin` and grant all privileges to the user admin
4. Create a database by the name `midstore` if it does not exist using the following sql command

```bash
CREATE DATABASE IF NOT EXISTS midstore encoding="utf-8";
```


# Developer set-up instructions

1. Clone the repository.
2. Checkout to branch `develop` by using command

```bash
git checkout develop
```

3. Install the requirements.txt file using command

```bash
pip install -r requirements.txt
```

4. Use the following command to run the migrations, which will create the required tables in the database.

```bash
python manage.py migrate
```

5. Use the following custom management command to migrate static data in database.

```bash
python manage.py data_migrate
```

6. Finally use the following command to start the development server.

```bash
python manage.py runserver
```

