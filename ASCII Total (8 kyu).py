'''
ASCII Total (8 kyu)
https://www.codewars.com/kata/572b6b2772a38bc1e700007a
'''

def uni_total(s):
    res = 0
    for item in s:
        res += ord(item)
    return res