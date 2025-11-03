from .models import Branch, Customer, Account, Transaction, Loan, LoanPayment
from django.utils import timezone
import random
from datetime import timedelta

def run():
    # Create branches
    branches = [
        Branch.objects.create(name="Salt Lake Main", location="Kolkata", ifsc_code="BK0001SLM"),
        Branch.objects.create(name="Park Street", location="Kolkata", ifsc_code="BK0002PS"),
        Branch.objects.create(name="Garia", location="Kolkata", ifsc_code="BK0003GA"),
    ]

    # Create customers
    customers = []
    for i in range(1, 11):
        customers.append(Customer.objects.create(
            first_name=f"Customer{i}",
            last_name="Test",
            email=f"customer{i}@bank.com",
            phone=f"99999{i:05d}",
            address="Kolkata, India",
            branch=random.choice(branches)
        ))

    # Create accounts
    accounts = []
    for cust in customers:
        acc = Account.objects.create(
            customer=cust,
            account_number=f"AC{random.randint(100000,999999)}",
            account_type=random.choice(['SAVINGS', 'CURRENT']),
            balance=random.uniform(1000, 50000)
        )
        accounts.append(acc)

    # Create transactions
    for acc in accounts:
        for _ in range(5):
            Transaction.objects.create(
                account=acc,
                transaction_type=random.choice(['DEPOSIT', 'WITHDRAWAL']),
                amount=random.uniform(100, 5000),
                description="Test transaction"
            )

    # Create loans
    loans = []
    for cust in random.sample(customers, 5):
        loan = Loan.objects.create(
            customer=cust,
            loan_amount=random.randint(50000, 200000),
            interest_rate=random.uniform(5, 12),
            start_date=timezone.now().date() - timedelta(days=random.randint(30, 300)),
            duration_months=random.choice([12, 24, 36])
        )
        loans.append(loan)

    # Create loan payments
    for loan in loans:
        for i in range(random.randint(2, 5)):
            LoanPayment.objects.create(
                loan=loan,
                payment_date=timezone.now().date() - timedelta(days=random.randint(5, 60)),
                payment_amount=loan.loan_amount / loan.duration_months,
                remarks="Monthly installment"
            )

    print("✅ Sample data created successfully!")
