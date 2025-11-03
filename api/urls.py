from rest_framework import routers
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'branches', BranchViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'loan-payments', LoanPaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
