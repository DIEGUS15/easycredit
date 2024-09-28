# easycredit_API

## Contributors

- Juan Camilo Banguero Melo - 1152098 - Username GitHub: juankmilo03
- Diego Alexander Granados Jaimes - 1152097 - Username GitHub: DiegoGranados15
- Angel Leonardo Montañez Corredor - 1152283 - Username GitHub: angelmontcorre

## EasyCreditApi - Backend

This project contains the backend for EasyCreditApi, a credit management web application developed with Django and SQLite. The backend provides a RESTful API that allows clients to interact with user and data.

## Installation

1. Clone this repository on your local machine:
bash
https://github.com/DIEGUS15/easycredit_API.git


2. Install the project dependencies:
bash
pip install -r requirements.txt

3. Perform database migrations:
bash
py manage.py makemigrations

bash
py manage.py migrate

4. Creating a Superuser
Once the migrations are complete, you can create a superuser with the following command:
bash
py manage.py createsuperuser

Follow the on-screen instructions to enter a username, email and password for the superuser.

5. Run the development server:
bash
py manage.py runserver

6. Enter the data you just created in the superuser and ready, you will have access to
