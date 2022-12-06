'''
Alphabetically ordered (7 kyu)
https://www.codewars.com/kata/5a8059b1fd577709860000f6
'''

def alphabetic(s):
    if len(s) == 0:
        return True
    save = ord(s[0])
    for item in s:
        print(ord(item))
        if save > ord(item):
            return False
        save = ord(item)
    return True