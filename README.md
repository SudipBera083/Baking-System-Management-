# 🏦 Banking System API

A **Django REST Framework** project that simulates a **core banking system**, including management of branches, customers, accounts, transactions, loans, and loan payments.  
It supports RESTful APIs to handle deposits, withdrawals, transfers, and loan payments.

---

## 🚀 Features

- Manage **branches**, **customers**, and **accounts**
- Perform **transactions** (Deposit, Withdrawal, Transfer)
- Manage **loans** and **loan payments**
- Auto-calculates remaining loan balance
- Clean and testable Django REST API structure

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.x |
| API Framework | Django REST Framework |
| Database | SQLite3 |
| Language | Python 3.11+ |
| Version Control | Git & GitHub |

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/SudipBera083/Baking-System-Management-.git
cd Banking-System-Management
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the development server
```bash
python manage.py runserver
```

Your API will now be available at:  
👉 **http://127.0.0.1:8000/**

---

## 🧾 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/branches/` | GET / POST | List or create branches |
| `/api/customers/` | GET / POST | List or create customers |
| `/api/accounts/` | GET / POST | Manage customer accounts |
| `/api/transactions/` | GET / POST | Record deposits, withdrawals, or transfers |
| `/api/loans/` | GET / POST | List or create loans |
| `/api/loan-payments/` | GET / POST | Manage loan payments |
| `/api/loan-payments/pay/` | POST | Make a payment towards a loan |

---

## 💳 Example Request

### ✅ POST `/api/loan-payments/pay/`

Make a payment toward an existing loan.

**Request Body:**
```json
{
  "loan_id": 1,
  "payment_amount": 2000.00,
  "remarks": "Monthly installment for November"
}
```

**Success Response:**
```json
{
  "message": "Payment of ₹2000.00 added successfully for Loan ID 1",
  "remaining_balance": 8000.00
}
```

**Error Response:**
```json
{
  "error": "Invalid loan_id or amount"
}
```

---

## 🗃️ Database Models

### 🏢 Branch
Holds branch information (name, IFSC, location)

### 👤 Customer
Customer personal details

### 💼 Account
Linked to a customer, tracks balance and type

### 💰 Transaction
Deposit, withdrawal, and transfer details

### 💸 Loan
Customer loans with amount, interest rate, and duration

### 🧾 LoanPayment
Tracks payments made toward a loan

---

## 🧩 Known Issues

### ❌ `/api/loan-payments/pay/` returning
```json
{"error": "Invalid loan_id or amount"}
```

**Cause:**  
Possible validation issue with `loan_id` or incorrect field mapping (`loan_amount` vs `amount`).

**Temporary Fix:**  
Ensure the `loan_id` exists and is valid before submitting the payment request.

---

## 🧠 Future Enhancements

- ✅ Add JWT authentication  
- ✅ Dashboard for admins  
- ✅ Add interest calculation logic for loans  
- ✅ Add transaction summaries per customer  

---

## 🤝 Contributing

1. **Fork** the repository  
2. **Create your feature branch**
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/your-feature
   ```
5. **Open a Pull Request** 🚀

---

## 👨‍💻 Author

**Sudip Bera**  
💼 Programmer Analyst @ Cognizant  
🔗 [Linkedin](https://www.linkedin.com/in/sudipbera083/)

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---
