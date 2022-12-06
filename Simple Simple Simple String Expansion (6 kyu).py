'''
Simple Simple Simple String Expansion (6 kyu)
https://www.codewars.com/kata/5ae326342f8cbc72220000d2
'''

def string_expansion(s):
    res = ""
    count = 1
    for index, item in enumerate(s):
        if item.isdigit():
            count = int(item)
        elif item.isalpha() and index != 0 and s[index-1].isalpha():
            res += item * count
        elif item.isalpha() and index != 0:
            res += item * int(s[index-1])
        elif item.isalpha():
            res += item
    return res