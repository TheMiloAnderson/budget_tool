from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Budget, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin


class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budget_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(budget__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['budget'] = Budget.objects.get(pk=self.kwargs['pk'])
        return context


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
