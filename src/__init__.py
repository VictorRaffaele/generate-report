from .base import Base
from .customers_info import CustomerInfo
from .employees_info import EmployeesInfo
from .sales_info import SalesInfo
import pandas as pd


def initialize_classes():
    base_instance = Base()

    # Read files to instance class
    file_customers, file_employees, file_order_datail, file_product, file_order = read_files()

    merged_orders_prod = pd.merge(file_order_datail, file_product)
    merged_orders_prod = merged_orders_prod.sort_values(by='product_id')
    orders = base_instance.divide_csv(merged_orders_prod, 'product_id')

    customer_info_instance = CustomerInfo(file_customers, file_order)
    employees_info_instance = EmployeesInfo(file_employees, file_order)
    sales_info_instance = SalesInfo(orders)

    return {
        'customer_info': customer_info_instance,
        'employees_info': employees_info_instance,
        'sales_info': sales_info_instance
    }


def read_files():
    file_customers = pd.read_csv('data/customers.csv', delimiter=';')
    file_employees = pd.read_csv('data/employees.csv', delimiter=';')
    file_order_datail = pd.read_csv('data/order_details.csv', delimiter=';')
    file_product = pd.read_csv('data/products.csv', delimiter=';')
    file_order = pd.read_csv('data/orders.csv', delimiter=';')

    return file_customers, file_employees, file_order_datail, file_product, file_order
