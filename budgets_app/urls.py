from django.urls import path
from .views import BudgetListView, TransactionListView, TransactionDetailView


urlpatterns = [
    path('', BudgetListView.as_view(), name='budgets'),
    path('<int:pk>', TransactionListView.as_view(), name='transactions'),
    path('transactions/<int:pk>', TransactionDetailView.as_view(), name='transaction')
]
