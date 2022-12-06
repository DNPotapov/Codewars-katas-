'''
Training JS #32: methods of Math---round() ceil() and floor() (8 kyu)
https://www.codewars.com/kata/5732d3c9791aafb0e4001236
'''

import math
def round_it(n):
    mass = str(n).split(".")
    if len(mass[0]) > len(mass[1]):
        return math.floor(n)
    elif len(mass[0]) < len(mass[1]):
        return math.ceil(n)
    else:
        return round(n)