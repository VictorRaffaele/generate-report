from base import Base
import pandas as pd


class CustomerInfo(Base):
    def __init__(self, customers: dict):
        self.__customers = customers

    def region(self) -> object:
        countrys = super().region(self.__customers)
        return countrys

    def n_purchases(self, df_orders: list[object], inverse=True) -> list[object]:
        merged_orders = pd.merge(df_orders, self.__customers)
        n_purchases = super().n_sales(merged_orders, 'customer_id', inverse)
        return n_purchases
