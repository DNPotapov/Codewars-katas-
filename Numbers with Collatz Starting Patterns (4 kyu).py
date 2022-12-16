"""
Numbers with Collatz Starting Patterns (4 kyu)
https://www.codewars.com//kata/5992e103b1429877bb00006b
"""

def collatz_steps(n, steps):
    while True:
        save = n
        for index, item in enumerate(steps):
            if item == 'D' and save % 2 == 0:
                save /= 2
            elif item == 'U' and save % 2 != 0:
                save = (3 * save + 1) / 2
            else:
                s_i = index
                break
        else:
            break
        n += 2 ** s_i
    return n