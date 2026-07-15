# 🏥 Hospital Management System

A full-stack Hospital Management System built with **FastAPI**, **MySQL**, and **Vanilla JS** frontend. It supports JWT-based authentication, role-based access control, and auto-logout after 2 days.

---

## 🚀 Tech Stack

### Backend
- **FastAPI** — Modern Python web framework
- **SQLAlchemy** — ORM for database management
- **Alembic** — Database migrations
- **MySQL** — Relational database
- **PyMySQL** — MySQL connector for Python
- **Pydantic** — Data validation
- **JWT (python-jose)** — Token-based authentication
- **Passlib (bcrypt)** — Password hashing

### Frontend
- **HTML5**
- **CSS3**
- **Vanilla JavaScript**
- **Fetch API** — Connect frontend to backend

---

## 📁 Project Structure
SAYLANI PROJECT/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── auth/
│   │   ├── init.py
│   │   ├── jwt.py
│   │   ├── hashing.py
│   │   └── dependencies.py
│   │
│   ├── crud/
│   │   ├── init.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── staff.py
│   │   └── user.py
│   │
│   ├── models/
│   │   ├── init.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── staff.py
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── init.py
│   │   ├── auth.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   └── staff.py
│   │
│   ├── schemas/
│   │   ├── init.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── staff.py
│   │   └── user.py
│   │
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── doctors.html
│   ├── patients.html
│   ├── staff.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── auth.js
│       ├── doctors.js
│       ├── patients.js
│       └── staff.js
│
├── alembic.ini
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hospital-management-system.git
cd hospital-management-system
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Create `.env` File
```env
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
DB_NAME=hospital_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_DAYS=2
```

### 5. Create MySQL Database
```sql
CREATE DATABASE hospital_db;
```

### 6. Run Migrations
```bash
python -m alembic revision --autogenerate -m "Create Tables"
python -m alembic upgrade head
```

### 7. Run the Server
```bash
uvicorn app.main:app --reload
```

### 8. Open Swagger UI
http://localhost:8000/docs

---

## 🔐 Authentication

- JWT Token based authentication
- Tokens expire after **2 days**
- Auto logout on frontend after token expiry
- Role based access control

### Roles
| Role | Access |
|---|---|
| Admin | Full access to everything |
| Doctor | Own data only |
| Staff | Limited access |

### Auth Endpoints
| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get token |
| POST | `/auth/refresh` | Refresh token |

---

## 📋 API Endpoints

### Doctor
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| GET | `/doctor/` | Get all doctors | ✅ Required |
| POST | `/doctor/` | Add new doctor | ✅ Required |
| GET | `/doctor/{id}` | Get doctor by ID | ✅ Required |
| PUT | `/doctor/{id}` | Update doctor | ✅ Required |
| DELETE | `/doctor/{id}` | Delete doctor | ✅ Required |

### Patient
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| GET | `/patient/` | Get all patients | ✅ Required |
| POST | `/patient/` | Add new patient | ✅ Required |
| GET | `/patient/{id}` | Get patient by ID | ✅ Required |
| PUT | `/patient/{id}` | Update patient | ✅ Required |
| DELETE | `/patient/{id}` | Delete patient | ✅ Required |

### Staff
| Method | Endpoint | Description | Auth |
|---|---|---|---|
| GET | `/staff/` | Get all staff | ✅ Required |
| POST | `/staff/` | Add new staff | ✅ Required |
| GET | `/staff/{id}` | Get staff by ID | ✅ Required |
| PUT | `/staff/{id}` | Update staff | ✅ Required |
| DELETE | `/staff/{id}` | Delete staff | ✅ Required |

---

## 🖥️ Frontend Pages

| Page | Description |
|---|---|
| `index.html` | Login page |
| `dashboard.html` | Main dashboard |
| `doctors.html` | Manage doctors |
| `patients.html` | Manage patients |
| `staff.html` | Manage staff |

---

## ✅ Features

### Completed
- [x] Project Structure
- [x] MySQL Database Setup
- [x] SQLAlchemy Models
- [x] Pydantic Schemas
- [x] CRUD Operations
- [x] REST API Routes
- [x] Alembic Migrations
- [x] Swagger Documentation

### In Progress
- [ ] JWT Authentication
- [ ] Role Based Access Control
- [ ] Protected Routes
- [ ] Frontend Login Page
- [ ] Frontend Dashboard
- [ ] Frontend Doctor/Patient/Staff Pages
- [ ] Connect Frontend to Backend API
- [ ] Auto Logout after 2 Days

---

## 🛠️ Requirements

fastapi
uvicorn
sqlalchemy
alembic
pydantic
pydantic-settings
pymysql
python-dotenv
mako
email-validator
python-jose[cryptography]
passlib[bcrypt]
python-multipart

---

## 👨‍💻 Developer

**Your Name**
- GitHub: [@vishalsahilai](https://github.com/vishalsahilai)

---

## 📄 License

This project is for educational purposes.