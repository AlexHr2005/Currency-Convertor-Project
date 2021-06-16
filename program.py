import requests

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
        print(output = "{} {}".format(round(self.curr_value, 2), self.curr_unit))

class Calculator():
    def __init__(self):
        pass

    def calculate(self, var1, var2, operation, requested_unit):
        new_value = 0
        if var1.curr_unit != requested_unit:
            var2.convert(requested_unit)

        if var2.curr_unit != requested_unit:
            var2.convert(requested_unit)

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
        print("{} {}".format(round(new_value, 2), requested_unit))

def convert(var):
    requested_unit = input("Enter the unit you want to convert in: ")
    var.convert(requested_unit)

def calculate(var1, var2):
    operation = input("Enter an operation: ")
    requested_unit = input("Enter the unit you want to calculate in: ")
    c = Calculator()
    c.calculate(var1, var2, operation, requested_unit)

var1 = Currency("USD", 10)
var2 = Currency("BGN", 14)

convert(var1)
calculate(var1, var2)