'''
L1: Set Alarm (8 kyu)
https://www.codewars.com/kata/568dcc3c7f12767a62000038
'''

def set_alarm(employed, vacation):
    return True if (employed and not vacation) else False