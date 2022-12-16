"""
Matunga coins (4 kyu)
https://www.codewars.com//kata/59799cb9429e83b7e500010c
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def min_price(coins):
    coins.sort()
    mass = [-1] * coins[0]
    mass[0] = 0

    for i in range(1, len(coins)):
        d = gcd(coins[0], coins[i])
        for r in range(d):
            ch = -1
            if r == 0:
                ch = 0
            else:
                q = r
                while q < coins[0]:
                    if mass[q] != -1 and (mass[q] < ch or ch == -1):
                        ch = mass[q]
                    q += d
            if ch != -1:
                for j in range(coins[0] // d):
                    ch += coins[i]
                    p = ch % coins[0]
                    if mass[p] != -1 and (mass[p] < ch or ch == -1):
                        ch = mass[p]
                    mass[p] = ch

    maximum = 0

    for i in range(coins[0]):
        if mass[i] == -1 or mass[i] > maximum:
            maximum = mass[i]

    if maximum == -1:
        return -1

    if maximum == 0:
        return 1

    return maximum - coins[0] + 1