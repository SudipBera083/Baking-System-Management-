# 🏦 Banking Management System (Django + SQLite)

A secure, full-stack web-based Banking Management System built using **Django** and **SQLite**.  
It provides essential banking operations such as account creation, deposits, withdrawals, transfers, and transaction statements with a responsive and modern UI.

---

## 📋 Features

- 🔐 **User Authentication** (Customer and Admin roles)
- 💰 **Deposit, Withdraw, and Transfer** operations
- 📄 **Transaction History / Statement**
- 🧾 **Account Management** (Balance tracking, account details)
- 🧍‍♂️ **Role-based Access** (Admin controls & Customer dashboard)
- 🗃️ **SQLite Database** (default for local dev)
- 🧠 **Secure Password + MPIN Hashing**
- 🌐 **Responsive Django Templates (Bootstrap/Tailwind UI)**

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5 / Tailwind CSS |
| **Backend** | Django 5.x (Python 3.10+) |
| **Database** | SQLite (development), can be migrated to PostgreSQL/MySQL |
| **Authentication** | Django Auth (with hashed MPIN for transactions) |
| **Version Control** | Git + GitHub |
| **Deployment (optional)** | Render / Vercel / Railway / Heroku |

---

## 🧱 Project Structure

banking_system/
├── banking/ # main project config (settings, urls)
├── accounts/ # app handling users & authentication
├── transactions/ # app for deposit, withdraw, transfer, statement
├── templates/ # HTML templates for views
├── static/ # CSS, JS, images
├── db.sqlite3 # SQLite database (auto created)
├── manage.py
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SudipBera083/Baking-System-Management-.git
cd Baking-System-Management

---

## ⚙️ Installation & Setup

### 1️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate       # on Linux/Mac
venv\Scripts\activate        # on Windows
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run migrations
```bash
python manage.py migrate
```

### 4️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 5️⃣ Run the development server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## 🧩 Core Django Apps

| App | Purpose |
|-----|----------|
| **accounts** | Handles registration, login, profile, and MPIN validation |
| **transactions** | Manages deposits, withdrawals, transfers, and history |
| **admin** | Built-in Django Admin for superuser operations |
| **api (optional)** | Future REST API endpoints using Django REST Framework |

---

## 🛡️ Security Highlights

- Passwords and MPINs are hashed using Django’s built-in PBKDF2.  
- CSRF protection, XSS protection, and SQL injection safety via Django ORM.  
- Role-based permissions to restrict unauthorized actions.

---

## 🧠 Future Enhancements

✅ Integrate Django REST Framework (DRF) for APIs  
✅ Add OTP-based verification for transactions  
✅ Add PDF export of account statements  
✅ Integrate real-time balance updates via AJAX  
✅ Add two-factor authentication (2FA)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🧑‍💻 Author

**Sudip Bera**  
💼 [LinkedIn](https://www.linkedin.com/in/sudipbera083/)  
📧 sudipbera083@gmail.com
