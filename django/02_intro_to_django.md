# 🚀 Day 2: Introduction to Django
**Your gateway to powerful web development with Python**

## 🎯 Learning Objectives
By the end of this lesson, you'll understand:
- What Django is and why it's popular
- Django's MVT (Model-View-Template) architecture
- How to set up your development environment
- How to create your first Django project and app
- The basic Django workflow

---

## 🔍 What is Django?

### The Definition
**Django** is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It was built by experienced developers to handle the common tasks of web development so you can focus on writing your app.

### Why Django is Awesome
- **🚀 Fast Development**: Built-in features for common tasks
- **🔒 Secure**: Protection against common security threats
- **📈 Scalable**: Can handle high traffic (used by Instagram, Pinterest)
- **🧩 Versatile**: Admin interface, user authentication, database ORM
- **📚 Well-Documented**: Excellent documentation and community

### What Django Includes Out of the Box
- User authentication system
- Admin panel for managing data
- Database abstraction layer (ORM)
- URL routing system
- Template engine
- Security features (CSRF, XSS protection)

---

## 🏗️ Django's MVT Architecture

Unlike traditional MVC (Model-View-Controller), Django uses **MVT** (Model-View-Template):

### 📊 Model (Data Layer)
- **Purpose**: Defines your data structure
- **Location**: `models.py`
- **Example**: User profiles, blog posts, products
- **What it does**: Interacts with the database

### 👀 View (Logic Layer)
- **Purpose**: Contains your business logic
- **Location**: `views.py`
- **Example**: Process form submissions, fetch data
- **What it does**: Receives requests, processes data, returns responses

### 🎨 Template (Presentation Layer)
- **Purpose**: Defines how data is displayed
- **Location**: `templates/` folder
- **Example**: HTML files with dynamic content
- **What it does**: Renders the final webpage

### 🔗 How They Work Together
```
User Request → URLs → View → Model (if needed) → Template → Response
```

---

## 🛠️ Setting Up Your Development Environment

### Prerequisites Check
Before we start, make sure you have:
- Python 3.8+ installed
- pip (Python package manager)
- A code editor (VS Code, PyCharm, etc.)

### Install Django
```bash
pip install django
```

### Verify Installation
```bash
django-admin --version
```

---

## 🎯 Your First Django Project

### Step 1: Create a Project
```bash
django-admin startproject mywebsite
cd mywebsite
```

### Step 2: Understand the Project Structure
```
mywebsite/
├── manage.py           # Command-line utility
├── mywebsite/
│   ├── __init__.py
│   ├── settings.py     # Project configuration
│   ├── urls.py         # URL routing
│   ├── wsgi.py         # Web server interface
│   └── asgi.py         # Async server interface
```

### Step 3: Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to see the Django welcome page! 🎉

---

## 📱 Creating Your First App

### What's the Difference: Project vs App?
- **Project**: Your entire website
- **App**: A specific feature/module (blog, shop, users)

### Step 1: Create an App
```bash
python manage.py startapp homepage
```

### Step 2: App Structure
```
homepage/
├── __init__.py
├── admin.py           # Admin interface config
├── apps.py            # App configuration
├── models.py          # Database models
├── tests.py           # Test cases
├── views.py           # View functions
└── migrations/        # Database changes
```

### Step 3: Register Your App
Add to `mywebsite/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',  # Add your app here
]
```

---

## 🌟 Your First View and URL

### Step 1: Create a View
In `homepage/views.py`:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My Django Website!</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1><p>This is our about page.</p>")
```

### Step 2: Create App URLs
Create `homepage/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

### Step 3: Connect to Main URLs
In `mywebsite/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
]
```

### Step 4: Test Your Pages
- Home page: `http://127.0.0.1:8000/`
- About page: `http://127.0.0.1:8000/about/`

---

## 🎨 Adding Templates

### Step 1: Create Template Directory
```
homepage/
└── templates/
    └── homepage/
        ├── base.html
        └── home.html
```

### Step 2: Create Base Template
In `homepage/templates/homepage/base.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Website{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
    </nav>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
</body>
</html>
```

### Step 3: Create Home Template
In `homepage/templates/homepage/home.html`:
```html
{% extends 'homepage/base.html' %}

{% block title %}Home - My Django Website{% endblock %}

{% block content %}
<h1>Welcome to My Django Website!</h1>
<p>This is the home page built with Django templates.</p>
{% endblock %}
```

### Step 4: Update Your View
In `homepage/views.py`:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')
```

---

## 🔧 Django's Built-in Features

### Admin Interface
```bash
python manage.py createsuperuser
```
Access at: `http://127.0.0.1:8000/admin/`

### Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Shell
```bash
python manage.py shell
```

---

## 🐛 Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'django'` | Install Django: `pip install django` |
| `ImportError: couldn't import Django` | Check if you're in the right directory |
| Template not found | Check template folder structure |
| `404 Page not found` | Verify URL patterns and view names |

---

## 📋 Django Development Workflow

1. **Plan your app structure**
2. **Create models** (database structure)
3. **Run migrations** (update database)
4. **Create views** (business logic)
5. **Design templates** (user interface)
6. **Configure URLs** (routing)
7. **Test your app**
8. **Deploy** (make it live)

---

## 🎯 What's Next?

In the upcoming lessons, we'll dive deeper into:
- **Models and Databases**: Store and retrieve data
- **Forms**: Handle user input
- **Authentication**: User registration and login
- **Static Files**: CSS, JavaScript, and images
- **Deployment**: Make your website live

---

## 📚 Essential Resources

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

---

## ✅ Practice Exercises

1. **Create a new app** called `blog` and add it to your project
2. **Create a contact view** that displays a simple contact form
3. **Add a footer** to your base template
4. **Create a projects page** showing a list of your projects
5. **Experiment with template inheritance** using `{% extends %}` and `{% block %}`

---

## 🏆 Congratulations!

You've successfully:
- ✅ Set up your first Django project
- ✅ Created your first app
- ✅ Built views and templates
- ✅ Configured URL routing
- ✅ Learned Django's MVT architecture

**You're now ready to build amazing web applications with Django!** 🚀

---

## 💡 Key Takeaways

- Django follows the MVT pattern (Model-View-Template)
- Projects contain apps, apps contain features
- Views handle the logic, templates handle the presentation
- URL routing connects web addresses to views
- Django provides many built-in features to speed up development

**Ready for Day 3? Let's build something awesome!** 🎉
