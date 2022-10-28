from django.test import TestCase
from .models import Employee

# Create your tests here.


class ModelsTestCase(TestCase):
    def test_employee(self):
        self.employee = Employee.objects.create(nom="Ndiaye", prenom='Mamadou', email='mamadou@test.com', adress="Yarakh")

    def model_employee(self):
        a = self.employee
        self.assertEqual(isinstance(a, Employee))


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)
