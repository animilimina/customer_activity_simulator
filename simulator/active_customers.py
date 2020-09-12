import pandas as pd
from simulator.customer import Customer
from simulator.new_customers import NewCustomers
import settings


class ActiveCustomers:
    def __init__(self, periods: int):
        self.__periods = periods + 1
        self.__period_new_customers = NewCustomers(settings.new_customer_base,
                                                   self.__periods,
                                                   settings.growth_rate
                                                   ).get_period_values()
        self.__customer_id_multiplier = self.__get_customer_id_multiplier()
        self.__activity_table = self.__build_full_activity()

    def __get_customer_id_multiplier(self) -> int:
        i = 1
        highest_new = self.__get_highest_new_customers()
        while highest_new // 10**i > 0:
            i += 1
        return 10**i

    def __get_highest_new_customers(self) -> int:
        return max(self.__period_new_customers)

    @staticmethod
    def __create_activity_table() -> pd.DataFrame:
        return pd.DataFrame(columns=['customer_id', 'activity'])

    def __build_full_activity(self) -> pd.DataFrame:
        full_activity = self.__create_activity_table()
        for period in range(0, self.__periods):
            period_id = period + 1
            nb_new_customers = self.__period_new_customers[period]
            full_activity = full_activity.append(self.__build_activity_for_period_new_customers(period_id, nb_new_customers))
        return full_activity

    def __build_activity_for_period_new_customers(self, period_id, nb_new_customers) -> pd.DataFrame:
        period_activity = self.__create_activity_table()
        customer_id_prefix = period_id * self.__customer_id_multiplier
        for customer_id in range(customer_id_prefix, customer_id_prefix + nb_new_customers):
            period_activity = period_activity.append(self.__simulate_customer_activity(period_id, customer_id))
        return period_activity

    def __simulate_customer_activity(self, first_period: int, customer_id: int) -> pd.DataFrame:
        customer_activity = self.__create_activity_table()
        customer_activity['activity'] = Customer(first_period,
                                                 self.__periods,
                                                 settings.returning_rate,
                                                 settings.reactivation_rate,
                                                 settings.survival_rate
                                                 ).get_active_periods()
        customer_activity["customer_id"] = customer_id
        return customer_activity

    def save_activity_table_to_csv(self):
        self.__activity_table.to_csv('~/Downloads/ActiveUsers.csv', index=False)
        print('ActiveUsers.csv was created in the Downloads directory.')