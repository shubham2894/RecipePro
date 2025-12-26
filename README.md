# 🍽️ RecipePro

RecipePro is a simple Django-based web application created as my **first Django project** for learning and practice purposes.  
The project focuses on understanding core Django fundamentals such as authentication, CRUD operations, templates, and basic UI design.

---

## 📌 Project Overview

RecipePro allows users to:
- Register and log in securely
- Add recipes with name, description, and image
- Search recipes by name
- Update and delete existing recipes
- View recipes in a clean, user-friendly dashboard

This project helped me gain hands-on experience with **Django backend development** and **HTML/CSS frontend integration**.

---

## 🚀 Features

- 🔐 User authentication (Login / Logout / Register)
- 📝 Add, update, and delete recipes (CRUD)
- 🖼️ Image upload support
- 🔍 Search functionality
- 👤 Login-protected access
- 🎨 Clean and responsive UI
- 🛡️ CSRF protection

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (default Django database)  
- **Authentication:** Django Auth System  

---

## 📂 Project Structure (Simplified)

```text
RecipePro/
├── manage.py
├── db.sqlite3
│
├── RecipePro/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── recipe/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── apps.py
│
├── templates/
│   ├── home.html
│   ├── landing_page.html
│   ├── login.html
│   ├── register.html
│   └── update_recipe.html
│
└── static/
    └── recipe/
