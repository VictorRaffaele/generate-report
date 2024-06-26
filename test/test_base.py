import unittest
import pandas as pd
from src.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        self.csv_path = 'test/files/employee.csv'
        self.csv = pd.read_csv(self.csv_path, delimiter=';')
        self.base = Base()

    def test_divide_csv(self):
        expected_result = [
            {
                'employee_id': [1],
                'last_name': ['Davolio'],
                'first_name': ['Nancy'],
                'country': ['USA'],
                'reports_to': [2.0]

            },
            {
                'employee_id': [2],
                'last_name': ['Fuller'],
                'first_name': ['Andrew'],
                'country': ['UK'],
                'reports_to': [2.0]
            }
        ]
        result = self.base.divide_csv(self.csv, 'employee_id')

        self.assertEqual(result[0].to_dict('list'), expected_result[0])
        self.assertEqual(result[1].to_dict('list'), expected_result[1])

    def test_region(self):
        expected_result = {'USA': 1, 'UK': 1}
        result = self.base.region(self.csv)

        self.assertEqual(expected_result, result)

    def test_n_sales(self):
        order_path = 'test/files/order.csv'
        order = pd.read_csv(order_path, delimiter=';')
        merged_order = pd.merge(self.csv, order)

        expected_result = [
            {'id': 1, 'name': 'Davolio, Nancy', 'n_sales': 1},
            {'id': 2, 'name': 'Fuller, Andrew', 'n_sales': 1}
        ]
        result = self.base.n_sales(merged_order, 'employee_id', True)

        self.assertEqual(expected_result, result)
