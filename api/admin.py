from django.contrib import admin
from .models import Branch, Customer, Account, Transaction, Loan, LoanPayment


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ifsc_code', 'location')
    search_fields = ('name', 'ifsc_code', 'location')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'branch')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('branch',)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_number', 'customer', 'account_type', 'balance', 'created_at')
    search_fields = ('account_number', 'customer__first_name', 'customer__last_name')
    list_filter = ('account_type', 'created_at')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'transaction_type', 'amount', 'timestamp')
    search_fields = ('account__account_number',)
    list_filter = ('transaction_type', 'timestamp')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'loan_amount', 'interest_rate', 'start_date', 'duration_months')
    search_fields = ('customer__first_name', 'customer__last_name')


@admin.register(LoanPayment)
class LoanPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan', 'payment_date', 'payment_amount')
    list_filter = ('payment_date',)
