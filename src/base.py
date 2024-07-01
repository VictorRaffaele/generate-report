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

    def n_sales(self, merged_orders: list[object], id_key: str, inverse: bool) -> list[object]:
        sales_divide = self.divide_csv(merged_orders, id_key)
        sales = []

        for sale in sales_divide:
            sales.append(self.generate_sales_object(sale, id_key))

        return sorted(sales, key=lambda key: key["n_sales"], reverse=inverse)

    def generate_sales_object(self, sale: object, id_key: str):
        if id_key == 'customer_id':
            return {
                'id': sale[id_key].iloc[0],
                'company_name': sale['company_name'].iloc[0],
                'n_sales': len(sale),
                'contact_name': sale['contact_name'].iloc[0],
                'phone': sale['phone'].iloc[0]
            }
        else:
            last_name = sale['last_name'].iloc[0]
            first_name = sale['first_name'].iloc[0]

            return {
                'id': int(sale[id_key].iloc[0]),
                'name': f'{last_name}, {first_name}',
                'n_sales': len(sale)
            }
