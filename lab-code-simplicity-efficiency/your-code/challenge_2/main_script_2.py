"""
The code below generates a given number of random strings that consists of numbers and
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import inputs_gen as inp
import random_str as rs


import inputs_gen as inp
import batch_gen as ba

n,a,b = inp.inputs_gen()

ba.batch_str_gen(n, a, b)
