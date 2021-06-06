import tkinter
import requests
import unittest

class Currency():
    def __init__(self, curr_unit, curr_value):
        self.curr_unit = curr_unit
        self.curr_value = curr_value

    def convert(self, requested_unit):
        url = "https://v6.exchangerate-api.com/v6/22b90070913b284544679858/latest/" + self.curr_unit
        j = requests.get(url).json()
        rates = j["conversion_rates"]
        self.curr_value = self.curr_value * rates[requested_unit]
        self.curr_unit = requested_unit

    def print(self):
        print("{} {}".format(self.curr_value, self.curr_unit))

class Calculator():
    def __init__(self):
        pass
    
    def calculate(self, var1, var2, operation, requested_unit):
        if var1.curr_unit != requested_unit:
            var2.convert(requested_unit)

        if var2.curr_unit != requested_unit:
            var2.convert(requested_unit)

        new_value = 0
        if operation == '+':
            new_value = var1.curr_value + var2.curr_value
        elif operation == '-':
            new_value = var1.curr_value - var2.curr_value
        elif operation == '*':
            new_value = var1.curr_value * var2.curr_value
        elif operation == '/':
            new_value = var1.curr_value / var2.curr_value
        elif operation == '//':
            new_value = var1.curr_value // var2.curr_value
        elif operation == '%':
            new_value = var1.curr_value % var2.curr_value
        print("{} {}".format(new_value, requested_unit))