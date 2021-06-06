import tkinter
import requests
from tkinter import Label
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
        Label(tk, text = str(self.curr_value)).pack()

value = Currency("USD", 18)

tk = tkinter.Tk()
tk.title("Currency Convertor")

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text = "Convert", command = lambda: value.convert(str(entry.get())))
button.pack()

tk.mainloop()