"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""
import inputs as inp
import operations as op

#print(op.math_operation(lst=inp.inputs_calc()))


input_list = inp.inputs_calc()

if type(input_list) == list:
    print(op.math_operation(lst=input_list))