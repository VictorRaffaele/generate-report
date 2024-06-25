import unittest
import pandas as pd
from src.sales_info import SalesInfo


class TestSalesInfo(unittest.TestCase):
    def setUp(self):
        self.orders = [
            pd.DataFrame({
                'product_id': [1, 1, 1],
                'product_name': ['Product A', 'Product A', 'Product A'],
                'quantity': [10, 20, 30],
                'unit_price': [100.0, 100.0, 75.0],
                'discount': [0.0, 10.0, 0.0]
            }),
            pd.DataFrame({
                'product_id': [2, 2],
                'product_name': ['Product B', 'Product B'],
                'quantity': [10, 20],
                'unit_price': [60.0, 60.0],
                'discount': [0.0, 6.0]
            }),
            pd.DataFrame({
                'product_id': [3, 3],
                'product_name': ['Product C', 'Product C'],
                'quantity': [15, 25],
                'unit_price': [120.0, 120.0],
                'discount': [0.0, 6.0]
            })
        ]

        self.sales_info = SalesInfo(self.orders)

    def test_products_solds(self):
        expected_result = [
            {'product_id': 1, 'product_name': 'Product A', 'total_sold': 60, 'total_amount': 5050.0},
            {'product_id': 3, 'product_name': 'Product C', 'total_sold': 40, 'total_amount': 4650.0},
            {'product_id': 2, 'product_name': 'Product B', 'total_sold': 30, 'total_amount': 1680.0}
        ]
        result = self.sales_info.products_solds('total_amount', 3)

        self.assertEqual(result, expected_result)

    def test_inverse_products_sold(self):
        expected_result = [
            {'product_id': 2, 'product_name': 'Product B', 'total_sold': 30, 'total_amount': 1680.0},
            {'product_id': 3, 'product_name': 'Product C', 'total_sold': 40, 'total_amount': 4650.0},
            {'product_id': 1, 'product_name': 'Product A', 'total_sold': 60, 'total_amount': 5050.0}
        ]
        result = self.sales_info.products_solds('total_amount', 3, False)

        self.assertEqual(result, expected_result)

    def test_total_amount(self):
        order = self.orders[0]
        expected_total = 5050.0
        total = self.sales_info.total_amount(order)

        self.assertEqual(total, expected_total)


if __name__ == '__main__':
    unittest.main()
