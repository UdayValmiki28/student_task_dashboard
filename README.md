![Student & Task Management Dashboard Banner](./frontend/public/github-banner.png)

# 🎓 Student & Task Management Dashboard

A *Full Stack Student & Task Management Dashboard* built with *Django (Backend)* and *React (Frontend)*.  
This application helps manage students, assign tasks, and track progress through an interactive dashboard with real-time statistics and charts.

---

## 🚀 Features

✅ *Student Management* — Add, update, or delete student records.  
✅ *Task Management* — Create and assign tasks to students, update task status.  
✅ *Interactive Dashboard* — Displays total students, tasks, and status insights via dynamic charts.  
✅ *SweetAlert2 Notifications* — Beautiful alerts for add/update/delete actions.  
✅ *Responsive Design* — Works seamlessly on desktop, tablet, and mobile devices.  
✅ *React + Django REST API Integration* — Frontend and backend communicate via clean API endpoints.

---

## 🛠 Tech Stack

### *Frontend*
- React.js ⚛  
- Axios (for API requests)  
- Recharts (for graphs)  
- SweetAlert2 (for alerts)  
- CSS3 (external responsive design)

### *Backend*
- Django 🐍  
- Django REST Framework (API)  
- SQLite3 (default database)

---

## 🧩 Project Structure

student_task_dashboard/
│
├── backend/ # Django backend folder
│ ├── api/ # REST API app (students & tasks)
│ ├── db.sqlite3 # Database
│ └── manage.py
│
├── frontend/ # React frontend folder
│ ├── src/
│ │ ├── components/
│ │ │ ├── StudentList.jsx
│ │ │ ├── TaskList.jsx
│ │ │ ├── students.css
│ │ │ ├── tasks.css
│ │ ├── Dashboard.jsx
│ │ ├── dashboard.css
│ │ ├── App.js
│ ├── package.json
│
└── README.md


---

## ⚙ Installation & Setup Guide

### 1️⃣ *Backend Setup (Django)*

```bash
cd backend
python -m venv myenv
myenv\Scripts\activate   # (Windows)
# or source myenv/bin/activate (Mac/Linux)

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Your Django server will run at:
👉 http://127.0.0.1:8000/

2️⃣ Frontend Setup (React)
cd frontend
npm install
npm start


Your React app will run at:
👉 http://localhost:3000/

📊 Dashboard Overview

The dashboard displays:

Total Students

Total Tasks

Pending Tasks

Completed Tasks

Includes two visualizations:

Pie Chart → Task completion ratio

Bar Chart → Tasks assigned per student

💡 SweetAlert2 Notifications

You’ll see alerts for:

✅ Student added successfully

🗑 Task deleted

✏ Record updated

(You can customize these in the respective component files.)

👨‍💻 Author

Developed by: Uday Kumar K S
GitHub: https://github.com/UdayValmiki28
Tech Stack: Django + React

🏁 Future Enhancements

🚀 Add Search & Filter options
🌙 Add Dark Mode
🍔 Add Collapsible Navbar for mobile
💬 Add Toast Notifications
📅 Add Due Dates for Tasks

🏆 Project Status

✅ Completed — Fully functional and responsive
🔄 Future scope: UX improvements and extra features