from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Branch, Customer, Account, Transaction, Loan, LoanPayment
from .serializers import *


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    # ✅ Search Branch by IFSC Code
    @action(detail=False, methods=['get'], url_path='search-by-ifsc')
    def search_by_ifsc(self, request):
        ifsc = request.query_params.get('ifsc', '').upper()
        if not ifsc:
            return Response({'error': 'IFSC code is required'}, status=400)
        try:
            branch = Branch.objects.get(ifsc_code__iexact=ifsc)
            serializer = self.get_serializer(branch)
            return Response(serializer.data)
        except Branch.DoesNotExist:
            return Response({'error': 'Branch not found'}, status=404)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # ✅ Get all accounts and loans of a customer
    @action(detail=True, methods=['get'])
    def overview(self, request, pk=None):
        customer = self.get_object()
        accounts = Account.objects.filter(customer=customer)
        loans = Loan.objects.filter(customer=customer)
        return Response({
            'customer': CustomerSerializer(customer).data,
            'accounts': AccountSerializer(accounts, many=True).data,
            'loans': LoanSerializer(loans, many=True).data,
        })

from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # ✅ Deposit money
    @action(detail=True, methods=['post'])
    def deposit(self, request, pk=None):
        account = self.get_object()
        try:
            amount = Decimal(request.data.get('amount', '0'))
        except:
            return Response({'error': 'Invalid amount format'}, status=400)

        if amount <= 0:
            return Response({'error': 'Invalid deposit amount'}, status=400)

        account.balance += amount
        account.save()

        Transaction.objects.create(
            account=account,
            transaction_type='Deposit',
            amount=amount
        )

        return Response({
            'message': f'Deposited ₹{amount}',
            'balance': str(account.balance)
        })

    # ✅ Withdraw money
    @action(detail=True, methods=['post'])
    def withdraw(self, request, pk=None):
        account = self.get_object()
        try:
            amount = Decimal(request.data.get('amount', '0'))
        except:
            return Response({'error': 'Invalid amount format'}, status=400)

        if amount <= 0:
            return Response({'error': 'Invalid withdrawal amount'}, status=400)
        if account.balance < amount:
            return Response({'error': 'Insufficient balance'}, status=400)

        account.balance -= amount
        account.save()

        Transaction.objects.create(
            account=account,
            transaction_type='Withdrawal',
            amount=amount
        )

        return Response({
            'message': f'Withdrew ₹{amount}',
            'balance': str(account.balance)
        })
    # ✅ View recent transactions
    @action(detail=True, methods=['get'])
    def transactions(self, request, pk=None):
        account = self.get_object()
        txns = Transaction.objects.filter(account=account).order_by('-timestamp')[:10]
        serializer = TransactionSerializer(txns, many=True)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-timestamp')
    serializer_class = TransactionSerializer


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Loan, LoanPayment
from .serializers import LoanSerializer, LoanPaymentSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        """Returns loan summary including payments."""
        loan = self.get_object()
        payments = LoanPayment.objects.filter(loan=loan)
        total_paid = sum(p.payment_amount for p in payments)
        remaining = loan.loan_amount - total_paid
        return Response({
            "loan_id": loan.id,
            "loan_amount": float(loan.loan_amount),
            "total_paid": float(total_paid),
            "remaining_balance": float(remaining),
            "is_fully_paid": remaining <= 0,
            "payments": LoanPaymentSerializer(payments, many=True).data
        })



class LoanPaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanPayment.objects.all()
    serializer_class = LoanPaymentSerializer

    # ✅ Make loan payment
    @action(detail=False, methods=['post'])
    def pay(self, request):
        loan_id = request.data.get('loan_id')
        amount = float(request.data.get('amount', 0))
        if not loan_id or amount <= 0:
            return Response({'error': 'Invalid loan_id or amount'}, status=400)

        try:
            loan = Loan.objects.get(id=loan_id)
        except Loan.DoesNotExist:
            return Response({'error': 'Loan not found'}, status=404)

        LoanPayment.objects.create(loan=loan, amount=amount)
        return Response({'message': f'Paid ₹{amount} for loan {loan_id}'})
