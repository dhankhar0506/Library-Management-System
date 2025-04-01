# 📚 Library Management System

## 🌟 Overview
The **Library Management System** is a web-based application built using **Django**, **HTML**, and **CSS**. This system allows users to manage library books and student records efficiently with CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features
- **🔐 User Authentication**: Secure login and registration system.
- **🛠 CRUD Operations**:
  - ➕ Add, 📖 view, ✏️ update, and ❌ delete student records.
  - ➕ Add, 📖 view, ✏️ update, and ❌ delete books.
- **📚 Book Management**: Store and manage book details such as title, author, publication date, and genre.
- **🎓 Student Management**: Register and manage students with unique registration numbers and contact details.

## 🛠 Tech Stack
- **Frontend**: 🎨 HTML, CSS
- **Backend**: 🐍 Django (Python)
- **Database**: 🗄 SQLite (default)

## 🗂 Models
The system contains the following models:

### 🎓 Student Model and 📖 Book Model
| Field Name      | Type     |
|----------------|---------- |
|publication_date| DateField |
| first_name     | CharField |
| last_name      | CharField |
| title          | CharField |
| Phone          | CharField |
| author         | CharField |
| genre          | CharField |
| view           | DateField |

## 🛠 Installation
1. **📥 Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Library-Management-System.git
   cd Library-Management-System
   ```
2. **💻 Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   On Windows use `venv\Scripts\activate`
   ```
3. **📦 Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **🔄 Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **👤 Create a superuser (Admin access)**:
   ```bash
   python manage.py createsuperuser
   ```
6. **🚀 Run the development server**:
   ```bash
   python manage.py runserver
   ```
7. **🌐 Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## 🎯 Usage
- ✅ Admin can log in and manage students and books.
- ✅ Users can view available books and details.
- ✅ Authentication ensures secure access.

---
### 👨‍💻 Author
Developed by **Gourav Dhankhar**

