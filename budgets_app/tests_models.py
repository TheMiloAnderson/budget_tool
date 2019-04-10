from django.test import TestCase
from budget_tool_project.factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='Red Bull',
            total_budget=234.56
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'Red Bull')
        self.assertEqual(self.budget.total_budget, 234.56)
