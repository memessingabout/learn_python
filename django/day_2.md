
🧠 Django Day 2 – Project Setup, Apps & URL Routing

> ✅ This guide walks you through creating your first Django app, setting up views, routing URLs, and rendering templates using Django's MVT architecture.

---

## 📌 Objectives

By the end of this session, you will:

* Create a Django project and app
* Understand Django's project/app structure
* Set up views and routes
* Render templates
* Handle common debugging errors

---

## 🧱 Step 1: Start a New Django Project

```bash
django-admin startproject mysite
cd mysite
python manage.py runserver
```

### 🔍 Project Structure

| File/Folder             | Purpose                                        |
| ----------------------- | ---------------------------------------------- |
| `manage.py`           | Command-line interface to interact with Django |
| `mysite/settings.py`  | Configuration (DB, apps, middleware, etc.)     |
| `urls.py`             | URL route declarations (entry point)           |
| `wsgi.py`/`asgi.py` | Server entry points                            |

---

## 🧩 Step 2: Create & Register an App

```bash
python manage.py startapp core
```

> 📍 Apps are modular components (like blog, auth, dashboard).

### ✅ Register it in `mysite/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'core',
]
```

---

## 🧠 Step 3: Create Views & Route URLs

### ✍️ `core/views.py`:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django World")
```

### 📍 `core/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### 🔗 Connect App URLs in `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

---

## 🎨 Step 4: Add Templates

### 📁 Folder Structure

```
core/
└── templates/
    └── core/
        └── home.html
```

### ✏️ `home.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Django Template</title>
</head>
<body>
    <h1>Welcome to My Django App</h1>
</body>
</html>
```

### 🔁 Update view in `core/views.py`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
```

---

## 🐞 Common Debugging Tips

| Problem              | Fix                                            |
| -------------------- | ---------------------------------------------- |
| `404 Not Found`    | Check if `urls.py`is included in root routes |
| Template not loading | Confirm correct folder structure & path        |
| `render()`error    | Use `from django.shortcuts import render`    |

---

## 🧪 Optional Bonus

* Use Django shell:
  ```bash
  python manage.py shell
  ```
* Explore `settings.py`:
  * `DEBUG`, `ALLOWED_HOSTS`
  * `TEMPLATES` and `INSTALLED_APPS`

---

## ✅ Wrap-Up Checklist

| ✅ | Task Completed                        |
| -- | ------------------------------------- |
| ✅ | Created project with `startproject` |
| ✅ | Built and registered app              |
| ✅ | Configured views and URLs             |
| ✅ | Rendered a template                   |

---

## 📚 Resources

* [📘 Django Intro: Official Docs](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
* [🧩 URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
* [🎨 Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/)
* [💡 Views &amp; Responses](https://docs.djangoproject.com/en/stable/topics/http/views/)

---

## 🔜 Coming Up – Day 3

* 📦 Working with Models
* 🔁 Running Migrations
* 🛠️ Django Admin Intro
* 🗂️ ORM Queries and Data Insertion
