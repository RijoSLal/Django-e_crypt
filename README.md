# e_crypt - SHA256 Password Generator

e_crypt is a web application built with Django and PostgreSQL that allows users to securely generate SHA256 hashed passwords. The app features a login and signup system for admin users, enabling them to manage and access the generated passwords.

## Features

- **User Authentication:**
  - Signup and login functionality for admin users.
  - Secure password storage using SHA256 hash.
  
- **Password Generation:**
  - Generate a secure SHA256 password hash from the user input.
  
- **Admin Panel:**
  - Admin can manage user data and passwords through the Django admin panel.

## Technologies Used

- **Backend:** Django
- **Database:** PostgreSQL
- **Hashing Algorithm:** SHA256
- **Authentication:** Django's built-in user authentication system

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Django 4.x
- PostgreSQL
- Pip (for installing dependencies)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/RijoSLal/e_crypt.git
   cd e_crypt
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:
   - Create a PostgreSQL database and user for the app.
   - Update the database credentials in `settings.py` under `DATABASES`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser for accessing the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Open the app in your browser:

   ```
   http://127.0.0.1:8000/
   ```

9. Login to the Django admin panel:

   ```
   http://127.0.0.1:8000/admin
   ```

## Usage

- **Generate SHA256 Password:**
  - Once logged in, users can input a password and the app will return its SHA256 hashed version.
  
- **Admin Panel:**
  - Admin users can manage user accounts and access the password generation tool from the admin panel.

## Contribution

Feel free to fork the repository, make improvements, and create pull requests. Contributions are always welcome!
