```markdown
# 🧠 Django Beginner Lesson – Day 1: Intro to Django & Web Servers

## 🎯 Learning Objectives
By the end of this lesson, you'll be able to:
- Explain how clients and servers communicate over the web.
- Understand basic HTTP methods.
- Describe Django and how it works.
- Understand MVT architecture.
- Recognize why Django is a powerful backend tool.

---

## 🔌 Web Server Basics

### What is a Server?
A server is a system that stores and serves **resources** like webpages, images, APIs.

### What is a Client?
A client (like a browser or mobile app) **accesses** those resources by making requests to the server.

---

## 🔁 Request-Response Cycle

- A **Client** makes a request to a **Server**.
- The **Server** processes the request and returns a **Response**.

### Common HTTP Methods:

| Method   | Description                                  | Example Use Case                     |
|----------|----------------------------------------------|--------------------------------------|
| `GET`    | Retrieves data from a resource                | Viewing a blog post                  |
| `POST`   | Submits data to a resource (creates data)     | Submitting a signup form            |
| `PUT`    | Replaces entire resource                      | Updating user profile info          |
| `PATCH`  | Updates partial resource                      | Editing a post caption              |
| `DELETE` | Deletes the specified resource                | Removing a comment                  |

### Example:
```http
POST /user
Content-Type: application/json

{
  "name": "Dom"
}
````

🔗 Reference: [MDN HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

---

## ⚙️ What is Django?

> Django is a **high-level Python web framework** that enables rapid development and clean design.

### Key Benefits:

* Python-based (clean syntax)
* Comes with batteries included (admin, auth, forms, etc.)
* Secure by default
* Uses ORM (no need for raw SQL)
* Scales well
* Popular among big tech (Instagram, YouTube)

---

## 🧩 MVT Architecture

| Component    | Purpose                           |
| ------------ | --------------------------------- |
| **Model**    | Manages the data (database logic) |
| **View**     | Handles the business logic        |
| **Template** | Defines the structure of the UI   |

---

## 🔄 Django Request-Response Flow

1. User makes a request: `www.myweb.com`
2. Django matches the URL in `urls.py`.
3. Passes control to the corresponding **view function**.
4. View runs logic and queries the **model** if needed.
5. View renders a **template** (HTML + data).
6. Sends final **HTML response** back to the browser.

---

## 🔐 Why Use Django?

✅ Built-in Admin Panel
✅ Built-in User Authentication
✅ CSRF Protection, SQL Injection Defense
✅ Django REST Framework for APIs
✅ ORM – Interact with DB using Python
✅ Actively maintained, widely supported

---

## 🧪 Live Demo (Optional)

### Start a new Django project:

```bash
django-admin startproject myproject
cd myproject
python manage.py runserver
```

### Visit:

`http://127.0.0.1:8000/`

---

## 📈 Django Ranks High

🔗 [Most Popular Backend Frameworks (2012–2025)](https://statisticsanddata.org/data/most-popular-backend-frameworks-2012-2025/)

Django is consistently ranked as one of the top frameworks, especially among Python developers.

---

## ✅ Recap Checklist

* [x] Server vs Client
* [x] HTTP Request Methods
* [x] Django Overview
* [x] MVT Architecture
* [x] Django Flow
* [x] Why Django is Loved

---

## 📚 Resources

* [Django Official Docs](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [MDN - HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

```
