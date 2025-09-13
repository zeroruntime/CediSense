# CediSense: Personal Finance Tracker (Django Web Application)

## Introduction

CediSense is a personal finance tracking web application built with Django.
It allows users to record income and expenses, set budgets, track savings goals, and analyze financial habits through a simple web interface.

---

## Features

* User authentication (registration, login, logout)
* Income and expense tracking
* Transaction categories
* Financial summaries and reports
* Responsive web interface using Django templates

---

## Technology Stack

* **Backend:** Django
* **Frontend:** Django Templates (HTML, CSS (Bootstrap 5), JavaScript)
* **Database:** PostgreSQL (or SQLite for development)

---

## Project Setup

### 1. Clone the Repository

```sh
git clone https://github.com/zeroruntime/cedisense.git
cd cedisense
```

### 2. Create and Activate Virtual Environment

```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure the Database

Update the database settings in **`settings.py`**.
By default, SQLite is enabled for development.

Apply migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```sh
python manage.py createsuperuser
```

### 6. Run the Development Server

```sh
python manage.py runserver
```

The application will be available at [http://localhost:8000](http://localhost:8000).

---

## Core Modules

* **User Management:** Registration, authentication, and profile management
* **Transactions:** Recording and managing income and expenses
* **Categories:** Organizing financial transactions
* **Reports:** Generating summaries and insights into financial activity with charts

---

## Future Enhancements

* Predictive financial insights
* Multi-currency support
* Shared expense management
* Advanced reporting with charts and visualizations

---

## License

MIT License © 2025 CediSense

---
