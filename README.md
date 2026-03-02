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
INSTALL GIT USING ANY BROWSER AND SETUP LOCALLLY 
THEN DO IT 

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
python -m venv venv #Create Virtual Environment
venv\Scripts\activate//activate envirnmemnt
pip install -r requirements.txt//install dependendice
//(if no requirments.txt their so create it )"pip freeze > requirements.txt"
//apply migrations
python manage.py makemigrations
python manage.py migrate

//AT LAST run the server
python manage.py runserver
