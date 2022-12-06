'''
Diff That Poly! (6 kyu)
https://www.codewars.com/kata/54f4b6e7576d7af70900092b
'''

def diff(poly):
    res = []
    for i, x in enumerate(poly[::-1]):
        if i != 0:
            res.append(x * i)
    return res[::-1]