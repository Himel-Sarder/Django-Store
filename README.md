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

    
# Deploy to Render
To deploy your Django project with **two apps** (`sale` and `predictor`) inside a parent project `car_sales` on **Render**, follow these step-by-step instructions. This guide includes static/media handling, environment setup, and Render-specific configuration.

---

### ✅ Folder Structure Assumption

```
project_folder/                ← Django project folder
├── manage.py
├── project/            ← Main project package (settings, urls)
├── app1/                 ← First app
├── app2/                 ← Second app
├── static/               ← Static files (optional)
├── media/                ← Media uploads (optional)
├── templates/            ← Global templates (optional)
├── requirements.txt
├── .env                  ← Local environment variables (ignored)
└── render.yaml           ← Deployment config for Render
```

---

## 🔧 1. Install Required Packages

In your virtual environment:

```bash
pip install gunicorn whitenoise dj-database-url psycopg2-binary
```

Then freeze:

```bash
pip freeze > requirements.txt
```

---

## ⚙️ 2. Update `settings.py`

### a. Allowed Hosts

```python
ALLOWED_HOSTS = ['.onrender.com']
```

### b. Static & Media Configuration

Add to `settings.py`:

```python
import os
import dj_database_url

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Whitenoise
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database from Render env var
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3', conn_max_age=600)
}
```

---

## 🗂 3. Add a `render.yaml`

In your root (`project/`) directory:

```yaml
services:
  - type: web
    name: car-sales
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn car_sales.wsgi:application
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: car_sales.settings
      - key: SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        fromDatabase:
          name: car_sales_db
          property: connectionString
    staticPublishPath: staticfiles
```

---

## 🛠 4. Create a Production `Procfile` (optional on Render)

```bash
echo "web: gunicorn <project_name>.wsgi:application" > Procfile
```

---

## 📂 5. Commit and Push to GitHub

Make sure your code is clean and pushed:

```bash
git init
git add .
git commit -m "Initial commit for Render deploy"
git remote add origin <your-github-repo-url>
git push -u origin main
```

---

## ☁️ 6. Set Up Render

1. Go to [https://render.com](https://render.com)
2. Click **"New + > Web Service"**
3. Connect your GitHub and select the repo
4. In Render settings:

   * Environment: `Python`
   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn <project_name>.wsgi:application`
   * Auto-deploy: Yes
5. Render will install & deploy

---

## 🧪 7. After Deployment (in Render Shell)

Run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

If needed:

```bash
python manage.py createsuperuser
```

---

## 📝 8. Optional: `.env` Support

Use Render's **Environment Variables UI** to set your `SECRET_KEY`, `DEBUG=False`, etc.

---

## ✅ 9. Done!

# Thank You 😻🩷
