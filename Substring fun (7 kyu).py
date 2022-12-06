'''
Substring fun (7 kyu)
https://www.codewars.com/kata/565b112d09c1adfdd500019c
'''

def nth_char(words):
    result = ""
    i = 0
    for item in words:
        result += item[i]
        i += 1
    return result