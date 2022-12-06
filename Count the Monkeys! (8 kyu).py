'''
Count the Monkeys! (8 kyu)
https://www.codewars.com/kata/56f69d9f9400f508fb000ba7
'''

def monkey_count(n):
    res = []
    for i in range(n):
        res.append(i+1)
    return res