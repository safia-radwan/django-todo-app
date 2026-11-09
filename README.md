# Django To-Do List App

A simple To-Do List web application built with Django.

## Features
- User registration and login.
- Add, edit, and delete tasks.
- Mark tasks as completed.
- View completed tasks.
- Each user can manage their own tasks.

## Technologies Used
- Python
- Django
- HTML
- CSS
- SQLite

## Installation

1. Clone the repository:
  
   git clone https://github.com/safia-radwan/django-todo-app.git
  

2. Navigate to the project directory.

3. Create a virtual environment:
  
   python -m venv venv
   

4. Activate the virtual environment:
  
   venv\Scripts\activate
   

5. Install dependencies:
   
   pip install django
   

6. Run migrations:
   
   python manage.py migrate

7. Install python-dotenv
  pip install django python-dotenv

8. Start the development server:
   
   python manage.py runserver

   
## Environment Variables

Create a `.env` file in the same directory as `manage.py`.

Add the following variable:

SECRET_KEY=your-secret-key-here

## Author
Safia Radwan
