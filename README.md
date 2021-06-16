# Currency-Convertor-Project

This is a school project for the "Introduction into script languages" classes, written on Python.
It's purpose is to convert from one currency unit into another and also to perform basic mathematical operations with these units.
There is not any type of GUI (graphical user interface) - everything is performed from the terminal.
Apart from the program itself (program.py), there is also a file with unit tests - unit_testing.py

In program.py there are 2 classes:
   -  Class Currency(), whose atributes are 'curr_unit' of type 'str' and 'curr_value' of type 'int'. 'curr_unit' represents the current unit of the variable
      and 'curr_value' - the current value of the variable.
      It has 2 methods (apart from __init__()):
          >convert(self, requested_unit) - it performes the convertion and takes as a parameter the unit in which the user wants to convert
          >print(self) - it prints the atributes of the variable in the following way: '[value] [unit]'
          
     *Note that there are already two defined variables of class Currency() - var1 and var2.
     
     The available units (and the representive exchange rates) for converting in are listed in here: https://v6.exchangerate-api.com/v6/22b90070913b284544679858/[unit],
     where [unit] is the unit from which the user wants to convert.
     
  -  Class Calculator(), which has no atributes - that means that the __init__() module is empty.
     It has 1 module (apart from __init__()):
        >calculate(self, var1, var2, operation, requested_unit) - it performes the mathematical operation and takes as parameters 2 variables of class Currency(), 
         with which the mathematical operation will be performed, the operation to be performed and the unit in which the result will be converted.
         
        *Note that there are only 6 supported mathematical operations: addition(+), subtraction(-), multiplication(*), division(/), modulus(%) and floor division(//)
         
         
In program.py there are also 2 functions:
  -  convert(var), which takes as a parameter 1 variable of class Currency() to be converted. 
     It asks the user to enter requested_unit via terminal and calls var.convert(self, requested_unit).
  -  calculate(var1, var2), which takes as parameters 2 variables of class Currency().
     It asks the user to enter the mathematical operation to be performed and requested_unit via terminal, creates a variable of class Calculator()
     and calls Calculator.calculate(self, var1, var2, operation, requested_unit).
     
In unit_testing.py there is 1 class:
  -  TestCurrency(unittest.TestCase), which inherits class TestCase from the unittest module. It has only 1 mothod:
        >test_currency_atributes(self), which checks whether the atributes of var1 and var2 are of the right type ('curr_unit' - of type 'str' and 'curr_value' - of type 'int')
