'''
(Ready for) Prime Time (5 kyu)
https://www.codewars.com//kata/521ef596c106a935c0000519
'''

def check_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


def prime(n):
    r = []
    for i in range(2, n+1):
        if check_prime(i) or i == 2:
            r.append(i)
    return r