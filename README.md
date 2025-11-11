
````markdown
# 🧪 QA Automation Challenge – Django Todo App (Param Purohit)

## 📋 Overview

This repository contains a Django-based **To-Do Application** with **end-to-end (E2E) automation tests** written in **Playwright (Python)**.

The application allows users to:
- Log in and manage tasks (Add, Complete, Delete)
- See only their own tasks (per-user isolation)
- View tasks paginated (5 per page)

✅ **All E2E tests (login, CRUD, isolation) pass successfully.**

---

## 🎯 Objectives Completed

1. ✅ Django app runs locally and supports authentication  
2. ✅ Added Playwright-based **UI automation tests** for:
   - Login / Logout  
   - Task CRUD (Add, Complete, Delete)  
   - User data isolation  
3. ✅ Pagination validated (no skipped or missing tasks)  
4. ✅ Fixed bugs:
   - Dashboard now filters tasks by logged-in user (`Task.objects.filter(user=request.user)`)
   - Pagination logic corrected  
5. ✅ Added reusable test helpers (`login`, `add_task`, `task_rows`)  

---

## 📸 Test Results Screenshot

You can include a screenshot here showing the **“3 tests passed”** output:

👉 **Replace the image below once uploaded**

![All Playwright Tests Passed](./docs/tests_passed.png)

---

## 🧰 Tech Stack

| Component | Tool |
|------------|------|
| Framework | **Django 5.2.8** |
| Language | **Python 3.11+** |
| Testing | **pytest + Playwright** |
| Database | SQLite (default) |
| Browser Automation | Chromium (Playwright) |

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Purohit1999/qa-automation-interview-param.git
cd qa-automation-interview-param/todo_app/qa-automation-interview
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Demo Users

For quick testing, run this one-liner:

```bash
python manage.py shell -c "from django.contrib.auth.models import User; \
u,_=User.objects.get_or_create(username='user1'); u.set_password('testpass123'); u.save(); \
v,_=User.objects.get_or_create(username='user2'); v.set_password('testpass123'); v.save(); \
print('Demo users created successfully')"
```

This creates:

* **user1 / testpass123**
* **user2 / testpass123**

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

Visit **[http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)**
Login using the credentials above.

---

## 🧪 Running the Tests

### 1️⃣ Install Playwright and pytest plugins

```bash
pip install pytest pytest-playwright playwright pytest-base-url
playwright install
```

### 2️⃣ Run the Local Server (in another terminal)

```bash
python manage.py runserver
```

### 3️⃣ Run All Tests

From the project root (where `tests/` folder exists):

```bash
pytest -q
```

Expected Output:

```
...                                                                 [100%]
3 passed in 5.4s
```

---

## ✅ Test Coverage Summary

| Test                           | Description                          |
| ------------------------------ | ------------------------------------ |
| `test_auth_logout`             | Verifies login & logout workflow     |
| `test_task_crud`               | Adds and deletes a task successfully |
| `test_isolation_between_users` | Confirms tasks are user-specific     |

---
## 📸 Test Results Screenshot
The **“3 tests passed”** output:


![All Playwright Tests Passed](./qa-automation-interview-param/docs/testpass.png)

---

## 🧩 Application Details

### `/login/`

* Authenticates users and redirects to dashboard

### `/dashboard/`

* Displays user’s tasks with pagination (5 per page)
* Supports task **Add**, **Complete**, and **Delete**
* Only shows tasks created by the logged-in user

### `/logout/`

* Safely logs users out and redirects to login page

---

## 🐞 Fixed Bugs

| Issue                             | Fix                                              |
| --------------------------------- | ------------------------------------------------ |
| All tasks visible to all users    | Filtered queryset by `user=request.user`         |
| Pagination skipping/offset errors | Corrected index slicing logic                    |
| Non-existent task deletion        | Wrapped `Task.DoesNotExist` with safe try/except |

---

## 📁 Project Structure

```
qa-automation-interview-param/
├── tests/
│   ├── pytest.ini
│   └── test_e2e.py
└── todo_app/
    └── qa-automation-interview/
        ├── manage.py
        ├── requirements.txt
        ├── tasks/
        │   ├── models.py
        │   ├── views.py
        │   ├── urls.py
        │   └── templates/tasks/
        │       ├── base.html
        │       ├── login.html
        │       └── dashboard.html
        └── todo_app/
            ├── settings.py
            ├── urls.py
            ├── asgi.py
            └── wsgi.py
```

---

## 💡 Bonus Improvements

* Added consistent message feedback using Django’s `messages` framework
* Isolated pagination logic (5 per page)
* User-friendly UI templates (Bootstrap-based)

---

## 📝 Submission Info

**Author:** Param Purohit
**Email:** [purohit.param91@gmail.com](mailto:purohit.param91@gmail.com)
**LinkedIn:** [https://www.linkedin.com/in/param-p-370616310/](https://www.linkedin.com/in/param-p-370616310/)
**Repo:** [https://github.com/Purohit1999/qa-automation-interview-param](https://github.com/Purohit1999/qa-automation-interview-param)

---

## 📞 Questions or Follow-up

If you’d like me to explain implementation details, test coverage, or design decisions, feel free to contact me by email or LinkedIn.

---

> *“Automated tests are the confidence behind every deploy.”* 🚀

````


