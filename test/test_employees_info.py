import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from src.employees_info import EmployeesInfo


class TestEmployeeInfo(unittest.TestCase):
    def setUp(self):
        self.csv_path = 'test/files/employee.csv'
        self.employees = pd.read_csv(self.csv_path, delimiter=';')
        self.employees_info = EmployeesInfo(self.employees)

    def test_region(self):
        expected_result = {'USA': 1, 'UK': 1}
        result = self.employees_info.region()

        self.assertEqual(expected_result, result)

    def test_supervision(self):
        supervises = pd.DataFrame({
            'employee_id': [1, 2],
            'last_name': ['Davolio', 'Fuller'],
            'first_name': ['Nancy', 'Andrew'],
            'country': ['USA', 'UK'],
            'reports_to': [2, 2]
        })
        expected_result = [
            {
                'name': 'Fuller, Andrew',
                'supervises': supervises,
                'count': 2
            }
        ]
        result = self.employees_info.supervision()

        for r, e in zip(result, expected_result):
            assert r['name'] == e['name']
            assert r['count'] == e['count']

            assert_frame_equal(r['supervises'], e['supervises'])

    def test_n_sales(self):
        order_path = 'test/files/order.csv'
        order = pd.read_csv(order_path, delimiter=';')
        merged_order = pd.merge(self.employees, order)

        expected_result = [
            {'id': 1, 'name': 'Davolio, Nancy', 'n_sales': 1},
            {'id': 2, 'name': 'Fuller, Andrew', 'n_sales': 1}
        ]
        result = self.employees_info.n_sales(merged_order, True)

        self.assertEqual(expected_result, result)
