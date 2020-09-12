from numpy.random import normal
import settings


class NewCustomers:
    def __init__(self, base: int, periods: int, average_growth: float):
        self.__base = base
        self.__periods = periods
        self.__average_growth = average_growth
        self.__period_values = []
        self.__build_period_values()

    def __build_period_values(self):
        base = self.__base
        sd = abs(1 - self.__average_growth) * 1.3
        for period in range(0, self.__periods):
            x = normal(self.__average_growth, sd)
            local_growth = max(x, settings.growth_rate_min)
            new_customers = round(base * local_growth)
            self.__period_values.append(new_customers)

    def get_period_values(self) -> list:
        return self.__period_values

