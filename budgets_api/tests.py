from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from budget_tool_project.factories import (
    UserFactory, BudgetFactory, TransactionFactory)
from budgets_app.models import Budget, Transaction


class TestUserAPI(APITestCase):
    def test_user_register_login(self):
        user = {
            'username': 'tester',
            'email': 'test@test.com',
            'password': '12345'
        }
        register_res = self.client.post('/api/v1/register', user, format='json')
        self.assertEqual(register_res.status_code, 201)
        user_res = self.client.get('/api/v1/user/' + str(register_res.data['id']))
        self.assertEqual(user_res.data['username'], 'tester')
        login_res = self.client.post('/api/v1/login', user)
        self.assertEqual(login_res.status_code, 200)
        self.assertTrue(len(login_res.data['token']) > 30)


class TestBudgetAPI(APITestCase):
    def setUp(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        self.user = User.objects.get(username='test_user')

    def test_create_budget(self):
        budget = {
            'name': 'red bull',
            'user': self.user,
            'total_budget': '200'
        }
        res = self.client.post('/api/v1/budgets', budget)
        self.assertTrue(b'red bull' in res.data)
        saved_budget = Budget.objects.get(id=res.data['id'])
        self.assertTrue(saved_budget.name == 'red bull')

    def test_return_budgets(self):
        budget = {
            'name': 'red bull',
            'user': self.user,
            'total_budget': '200'
        }
        res = self.client.post('/api/v1/budgets', budget)
        token = '"Authorization: Token ' + str(self.user.auth_token) + '"'
        res = self.client.get('/api/v1/budgets ' + token)
        self.assertTrue(res.data['name'] == 'red bull')

    def test_not_logged_in(self):
        res = self.client.get('/api/v1/budgets')
        self.assertEqual(res.status_code == 404)
