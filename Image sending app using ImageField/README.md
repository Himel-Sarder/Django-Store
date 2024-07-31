## Directory Structure
![image](https://github.com/user-attachments/assets/77d455c5-abf0-4b9b-99be-0e8d64540742)


Adding an image field in Django involves several steps, including setting up your Django project and application, creating a model with an image field, configuring media settings, and creating templates and views to upload and display images. Here’s a step-by-step guide with the directory structure:

### 1. Setting Up Your Django Project

First, create a new Django project if you don't already have one:

```bash
django-admin startproject ImageProject .
```

### 2. Creating a Django App

Create a new app within your project:

```bash
python manage.py startapp ImageSendingApp
```

### 3. Configuring Settings

In `ImageProject/settings.py`, add your app to the `INSTALLED_APPS` list and configure media settings:

```python
INSTALLED_APPS = [
    ...
    'ImageSendingApp',
    ...
]

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 4. Install pillow
```bash
pip install pillow
```

### 5. Creating the Image Model

In `ImageSendingApp/models.py`, create a model with an `ImageField`:

```python
from django.db import models

class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')
```

### 6. Migrating the Database

Create and apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Creating Forms

Create a form for uploading images. In `ImageSendingApp/forms.py`:

```python
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['image']
```

### 8. Creating Views

In `ImageSendingApp/views.py`, create views to handle image upload and display:

```python
from django.shortcuts import render, redirect
from .forms import MyModelForm
from .models import MyModel

def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = MyModelForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = MyModel.objects.all()
    return render(request, 'image_list.html', {'images': images})
```

### 9. Configuring URLs

In `ImageProject/urls.py`, include your app's URLs and configure media URL serving:

```python
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

In `ImageSendingApp/urls.py`, define the URLs for the views:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('upload/', views.upload_image, name='upload_image'),
]
```

### 10. Creating Templates

Create templates for uploading and displaying images.

`ImageSendingApp/templates/upload_image.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Upload Image</title>
</head>
<body>
    <h1>Upload Image</h1>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

`ImageSendingApp/templates/image_list.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Image List</title>
</head>
<body>
    <h1>Image List</h1>
    <a href="{% url 'upload_image' %}">Upload New Image</a>
    <ul>
        {% for image in images %}
        <li>
            <img src="{{ image.image.url }}" alt="Image" style="width: 200px; height: auto;">
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

### 11. Running the Server

Run your development server to test the functionality:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/upload/` to upload an image and `http://127.0.0.1:8000/` to see the list of uploaded images.
