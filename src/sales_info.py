class SalesInfo:
    def __init__(self, orders: list[object]):
        self.__orders = orders

    def products_solds(self, sort_key: str, num_lines: int) -> list:
        arr = []

        for order in self.__orders:
            sales = self.divide_sales_column(order, 'unit_price')
            discount = self.divide_sales_column(order, 'discount')
            total_sold = int(order['quantity'].sum())
            total_price = float(self.total_amount(sales))
            total_discount = float(self.total_amount(discount))

            arr.append({
              'product_id': int(order['product_id'].iloc[0]),
              'product_name': order['product_name'].iloc[0],
              'total_sold': total_sold,
              'total_amount': total_price - total_discount
            })

        return sorted(arr, key=lambda key: key[f"{sort_key}"], reverse=True)[:num_lines]

    def total_amount(self, order: object) -> float:
        count = order['count']
        prices = order['prices']
        sales_count = order['sale_count']

        total = 0

        for each in range(count):
            total += (prices.iloc[each] * sales_count.iloc[each]).round(2)

        return total

    def divide_sales_column(self, order: object, key: str) -> dict:
        unique_prices = order[f'{key}'].value_counts().reset_index()
        unique_prices.columns = [f'{key}', 'count']

        prices = unique_prices[f'{key}']
        sale_count = unique_prices['count']
        count = int(unique_prices.value_counts().iloc[0])

        return {'prices': prices, 'sale_count': sale_count, 'count': count}
