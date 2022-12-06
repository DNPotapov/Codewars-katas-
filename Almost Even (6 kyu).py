'''
Almost Even (6 kyu)
https://www.codewars.com/kata/529e2e1f16cb0fcccb000a6b
'''

def split_integer(num, parts):
    res = []
    if parts == 1:
        res.append(num)
    else:
        while parts > 0:
            res.append(num // parts)
            num = num - num // parts
            parts = parts - 1
    return res