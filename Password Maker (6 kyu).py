'''
Password Maker (6 kyu)
https://www.codewars.com/kata/5b3d5ad43da310743c000056
'''

import random
def randletter(x, y):
    return chr(random.randint(ord(x), ord(y)))
def make_password(length, flag_upper, flag_lower, flag_digit):
    res = ""
    count = 0
    while length > 0:
        if flag_upper and length > 0:
            ran = randletter('A', 'Z')
            while (ran in res):
                ran = randletter('A', 'Z')
            res += ran
            length = length - 1
        if flag_lower and length > 0:
            ran = randletter('a', 'z')
            while (ran in res):
                ran = randletter('a', 'z')
            res += ran
            length = length - 1
        if flag_digit and length > 0 and count < 10:
            count += 1
            ran = str(random.randint(0, 9))
            while (ran in res):
                ran = str(random.randint(0, 9))
            res += ran
            length = length - 1
    return res