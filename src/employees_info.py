import pandas as pd
from .base import Base


class EmployeesInfo(Base):
    def __init__(self, employees: dict, orders: dict):
        self.__employees = employees
        self.__orders = orders

    def region(self) -> object:
        countrys = super().region(self.__employees)
        return countrys

    def supervision(self) -> list[object]:
        employees_list = super().divide_csv(self.__employees, 'employee_id')
        supervisors_list = super().divide_csv(self.__employees, 'reports_to')
        supervisors = []

        for employee in employees_list:
            for supervisor in supervisors_list:
                employee_id = int(employee['employee_id'].iloc[0])
                supervisor_id = int(supervisor['reports_to'].iloc[0])

                if employee_id == supervisor_id:
                    last_name = employee['last_name'].iloc[0]
                    first_name = employee['first_name'].iloc[0]

                    supervisors.append({
                        'name': f'{last_name}, {first_name}',
                        'supervises': supervisor.to_dict(orient='records'),
                        'count': len(supervisor)
                    })

        return supervisors

    def n_sales(self, inverse=True) -> list[object]:
        merged_orders = pd.merge(self.__orders, self.__employees)
        n_sales = super().n_sales(merged_orders, 'employee_id', inverse)
        return n_sales
