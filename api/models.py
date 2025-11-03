from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    ifsc_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.name} ({self.ifsc_code})"


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="customers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Account(models.Model):
    ACCOUNT_TYPES = (
        ('SAVINGS', 'Savings'),
        ('CURRENT', 'Current'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="accounts")
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} ({self.customer})"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
        ('TRANSFER', 'Transfer'),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.account}"


class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="loans")
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    duration_months = models.IntegerField()

    def __str__(self):
        return f"Loan {self.id} - {self.customer}"


class LoanPayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="payments")
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=12, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment of {self.payment_amount} on {self.payment_date}"
