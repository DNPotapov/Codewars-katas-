'''
Char Code Calculation (7 kyu)
https://www.codewars.com/kata/57f75cc397d62fc93d000059
'''

def calc(x):
    result = ""
    for item in x:
        result += str(ord(item))
    return (sum([int(i) for i in result]) - sum([int(i) for i in result.replace("7","1")]))