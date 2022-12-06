'''
Find the calculation type (7 kyu)
https://www.codewars.com/kata/5aca48db188ab3558e0030fa
'''

def calc_type(a, b, res):
    if a+b == res:
        return "addition"
    elif a*b == res:
        return "multiplication"
    elif a-b == res:
        return "subtraction"
    else:
        return "division"