# 🌍 Disaster Management and Alert System

A web-based Disaster Management and Alert System built using Django and OpenStreetMap (Leaflet).

This project allows users to:
- Register and login
- Save their latitude and longitude
- View their location on an interactive map
- Manage disaster-related alerts

---

## 🚀 Features

- User Authentication (Login / Logout)
- Store User Location (Latitude & Longitude)
- Display User Location on OpenStreetMap
- Interactive Map using Leaflet.js
- Clean Responsive UI

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Map: Leaflet.js
- Map Tiles: OpenStreetMap
- Database: SQLite (default)

---

## 📦 Installation Guide

Follow these steps to clone and run the project locally.

### 1️⃣ Clone the Repository 
Make sure you have Git installed, then run:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 🤖 One-Click Setup with Antigravity AI
If you are using the **Antigravity AI**, you can instantly set up and run the code with a single command! Just type:
```bash
/setup
```
Antigravity will automatically create the virtual environment, install `requirements.txt`, run all database migrations, and start the local server!

### 💻 One-Click setup for Windows Users
If you are running this natively on Windows, we've provided a simple batch script to automate everything. Just double-click or run:
```bash
setup_and_run.bat
```

### 🛠️ Manual Installation (Advanced)
If you prefer doing it piece by piece, run the following:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
