import unittest
import pandas as pd
from src.employees_info import EmployeesInfo


class TestEmployeeInfo(unittest.TestCase):
    def setUp(self):
        self.csv_path = 'test/files/employee.csv'
        self.employees = pd.read_csv(self.csv_path, delimiter=';')
        self.order_path = 'test/files/order.csv'
        self.order = pd.read_csv(self.order_path, delimiter=';')
        self.employees_info = EmployeesInfo(self.employees, self.order)

    def test_region(self):
        expected_result = {'USA': 1, 'UK': 1}
        result = self.employees_info.region()

        self.assertEqual(expected_result, result)

    def test_supervision(self):
        supervises = [{
            'employee_id': 1,
            'last_name': 'Davolio',
            'first_name': 'Nancy',
            'country': 'USA',
            'reports_to': 2
        }, {
            'employee_id': 2,
            'last_name': 'Fuller',
            'first_name': 'Andrew',
            'country': 'UK',
            'reports_to': 2
        }]
        expected_result = [
            {
                'name': 'Fuller, Andrew',
                'supervises': supervises,
                'count': 2
            }
        ]
        result = self.employees_info.supervision()

        self.assertEqual(expected_result, result)

    def test_n_sales(self):
        expected_result = [
            {'id': 1, 'name': 'Davolio, Nancy', 'n_sales': 1},
            {'id': 2, 'name': 'Fuller, Andrew', 'n_sales': 1}
        ]
        result = self.employees_info.n_sales()

        self.assertEqual(expected_result, result)
