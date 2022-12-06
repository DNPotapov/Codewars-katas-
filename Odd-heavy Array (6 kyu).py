'''
Odd-heavy Array (6 kyu)
https://www.codewars.com/kata/59c7e477dcc40500f50005c7
'''

def is_odd_heavy(arr):
    odds = [i for i in arr if i%2]
    even = [i for i in arr if not i%2]
    if len(odds) == 0:
        return False
    if len(even) == 0:
        return True
    return min(odds) > max(even)