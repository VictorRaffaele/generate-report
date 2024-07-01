import unittest
import pandas as pd
from src.customers_info import CustomerInfo


class TestCustomersInfo(unittest.TestCase):
    def setUp(self):
        self.customer_path = 'test/files/customer.csv'
        self.customer = pd.read_csv(self.customer_path, delimiter=';')
        self.customer_info = CustomerInfo(self.customer)

    def test_region(self):
        expected_result = {'Brazil': 1, 'USA': 1}
        result = self.customer_info.region()

        self.assertEqual(expected_result, result)

    def test_n_purchases(self):
        order_path = 'test/files/order.csv'
        order = pd.read_csv(order_path, delimiter=';')
        merged_order = pd.merge(self.customer, order)

        expected_result = [
            {
                'id': 'AAAAA',
                'company_name': 'A Company',
                'n_sales': 1,
                'contact_name': 'A agent',
                'phone': '000-0000001'
            },
            {
                'id': 'BBBBB',
                'company_name': 'B Company',
                'n_sales': 1,
                'contact_name': 'B agent',
                'phone': '000-0000002'
            }
        ]
        result = self.customer_info.n_purchases(merged_order, True)

        self.assertEqual(expected_result, result)
