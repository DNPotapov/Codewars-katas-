'''
Caffeine Script (7 kyu)
https://www.codewars.com/kata/5434283682b0fdb0420000e6
'''

def caffeine_buzz(n):
    return "mocha_missing!" if n%3!=0 else "CoffeeScript" if n%2+n%3+n%4==0 else "JavaScript" if n%2+n%3==0 else "Java"
