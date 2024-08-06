Here’s a comprehensive list of necessary commands for various stages of Django development, from setting up a new project to managing the database and running the server.

### Setting Up a New Django Project

1. **Install Django:**
   ```bash
   pip install django
   ```

2. **Create a new Django project:**
   ```bash
   django-admin startproject projectname 
   cd projectname
   ```
   OR,
   ```bash
   django-admin startproject projectname .
   ```

### Creating and Managing Django Apps

3. **Create a new app within the project:**
   ```bash
   python manage.py startapp appname
   ```

### Database Migrations

4. **Make migrations (generate SQL from your models):**
   ```bash
   python manage.py makemigrations
   ```

5. **Apply the migrations to the database:**
   ```bash
   python manage.py migrate
   ```

### Creating a Superuser

6. **Create a superuser to access the Django admin interface:**
   ```bash
   python manage.py createsuperuser
   ```

### Running the Development Server

7. **Run the Django development server:**
   ```bash
   python manage.py runserver
   ```

### Managing Django Models

8. **Open the Django shell:**
   ```bash
   python manage.py shell
   ```

### Static Files and Media Files

9. **Collect static files (for deployment):**
   ```bash
   python manage.py collectstatic
   ```

### Testing

10. **Run tests:**
    ```bash
    python manage.py test
    ```

### Other Useful Commands

11. **Check for any problems in the project (like linting):**
    ```bash
    python manage.py check
    ```

12. **Create custom management commands:**
    ```bash
    python manage.py startapp appname
    ```

### Setting Up and Using a Virtual Environment

13. **Create a virtual environment:**
    ```bash
    python -m venv env
    ```

14. **Activate the virtual environment:**
    - On Windows:
      ```bash
      env\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source env/bin/activate
      ```

15. **Deactivate the virtual environment:**
    ```bash
    deactivate
    ```

### Installing and Freezing Requirements

16. **Install packages from a requirements file:**
    ```bash
    pip install -r requirements.txt
    ```

17. **Generate a requirements file:**
    ```bash
    pip freeze > requirements.txt
    ```

### Django Admin Commands

18. **Start a new app (creating models and initial files):**
    ```bash
    python manage.py startapp appname
    ```

19. **Show all available management commands:**
    ```bash
    python manage.py help
    ```

### Working with Django Models

20. **Inspect database schema:**
    ```bash
    python manage.py inspectdb
    ```

### Deployment-Specific Commands

21. **Create an initial migration for the database:**
    ```bash
    python manage.py makemigrations
    ```

22. **Run a specific migration:**
    ```bash
    python manage.py migrate appname migrationname
    ```

23. **Check for and display available migrations:**
    ```bash
    python manage.py showmigrations
    ```

24. **Rollback to a previous migration:**
    ```bash
    python manage.py migrate appname migrationname
    ```

These commands cover most of the day-to-day operations you’ll need when working with a Django project.

# Thank You 😻
