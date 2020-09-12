import settings
from random import random
from numpy.random import normal


class Customer:
    def __init__(self, first_period: int, last_period: int, average_returning_rate: float, average_reactivation_rate:float, average_survival_rate: float):
        self.__first_period = first_period
        self.__last_period = last_period
        self.__seniority = 0
        self.__returning_rate = self.__generate_rate(average_returning_rate)
        self.__reactivation_rate = self.__generate_rate(average_reactivation_rate)
        self.__survival_rate = self.__generate_rate(average_survival_rate)
        self.__is_active = True
        self.__is_alive = True
        self.__active_periods = []
        self.__list_active_periods()

    @staticmethod
    def __generate_rate(rate) -> float:
        sd = (1 - rate) / 2
        x = normal(rate, sd)
        return max(0, min(x, .99))

    def __list_active_periods(self):
        while self.__is_alive and self.__first_period + self.__seniority < self.__last_period:
            self.__test_if_active()
            self.__build_active_periods_list()
            self.__test_if_survives()
            self.__increase_seniority()

    def __test_if_active(self):
        if self.__seniority == 0:
            pass
        elif self.__is_active:
            self.__activity_if_previously_active()
        else:
            self.__activity_if_previously_inactive()

    def __activity_if_previously_active(self):
        if random() > self.__returning_rate:
            self.__is_active = False

    def __activity_if_previously_inactive(self):
        if random() <= self.__reactivation_rate:
            self.__is_active = True

    def __build_active_periods_list(self):
        if self.__is_active:
            self.__active_periods.append(self.__first_period + self.__seniority)

    def __test_if_survives(self):
        if random() > self.__survival_rate:
            self.__is_alive = False

    def __increase_seniority(self):
        self.__seniority += 1

    def get_active_periods(self) -> list:
        return self.__active_periods

