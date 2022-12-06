'''
A Strange Trip to the Market (8 kyu)
https://www.codewars.com/kata/55ccdf1512938ce3ac000056
'''

def is_lock_ness_monster(string):
    mass = ['3.50', 'tree fiddy', 'three fifty']
    for item in mass:
        if item in string:
            return True
    return False