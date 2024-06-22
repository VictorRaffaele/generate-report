class SalesInfo:
    def __init__(self, orders: list[object]):
        self.__orders = orders

    def products_solds(self, sort_key: str, num_lines: int) -> list:
        arr = []

        for order in self.__orders:
            total_sold = int(order['quantity'].sum())
            total_price = float(self.total_amount(order))

            arr.append({
              'product_id': int(order['product_id'].iloc[0]),
              'product_name': order['product_name'].iloc[0],
              'total_sold': total_sold,
              'total_amount': total_price
            })

        return sorted(arr, key=lambda key: key[f"{sort_key}"], reverse=True)[:num_lines]

    def total_amount(self, order: object) -> float:
        total = 0

        for quantity, unit_price, discount in zip(order['quantity'], order['unit_price'], order['discount']):
            total += ((unit_price - discount) * quantity)

        return total
