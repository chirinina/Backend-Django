# 🌿 EcoApp

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Django-Framework-green?logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite&logoColor=blue" />
  <img src="https://img.shields.io/badge/Environment-Virtualenv-orange?logo=python&logoColor=white" />
</p>

---

##  Project Overview

**EcoApp** is a web-based application built with **Django**, designed to manage inventory efficiently and support scalable development practices.

> Developed by **Efrain Chiri**

---

## ⚙️ Requirements

Before starting, ensure you have the following installed:

- Python 3.10+
- pip (Python package manager)
- Virtual Environment (recommended)

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ecoapp
```

### 2. Create virtual environment

```bash
python -m venv entorno
```

### 3. Activate virtual environment

- **Linux / MacOS**

```bash
source entorno/bin/activate
```

- **Windows**

```bash
entorno\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Development Server

Run the development server:

```bash
python manage.py runserver
```

Access the application at:

```
http://127.0.0.1:8000/
```

---

##  Superuser Creation

Create an administrator account:

```bash
python manage.py createsuperuser
```

---

##  Load Initial Data

Import initial inventory data:

```bash
python manage.py loaddata dump_inventario.json
```

---

##  Author

**Efrain Chiri**
Dev

---

## License

This project is for educational and professional use.
