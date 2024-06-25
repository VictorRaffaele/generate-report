import pandas as pd


class Base:
    def divide_csv(self, csv, value: str) -> list:
        df = pd.DataFrame(csv)
        return [group for _, group in df.groupby(value)]

    def region(self, data_frame: list[object]) -> object:
        countrys = self.divide_csv(data_frame, 'country')
        country = {}

        for each in countrys:
            country_name = each['country'].iloc[0]
            num_employees = len(each)
            country.update({f'{country_name}': num_employees})

        return country

    def n_sales(self, merged_orders: list[object], order) -> list[object]:
        sales_divide = self.divide_csv(merged_orders, 'employee_id')
        sales = []

        for sale in sales_divide:
            last_name = sale['last_name'].iloc[0]
            first_name = sale['first_name'].iloc[0]

            sales.append({
                'id': int(sale['employee_id'].iloc[0]),
                'name': f'{last_name}, {first_name}',
                'n_sales': len(sale)
            })

        return sorted(sales, key=lambda key: key["n_sales"], reverse=order)
