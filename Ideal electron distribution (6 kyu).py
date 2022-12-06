'''
Ideal electron distribution (6 kyu)
https://www.codewars.com/kata/59175441e76dc9f9bc00000f
'''

import math
def atomic_number(electrons):
    if round(math.sqrt(electrons/2))+1 - math.sqrt(electrons/2) > 0:
        chislo_obolochek = round(math.sqrt(electrons/2))+1
    else:
        chislo_obolochek = round(math.sqrt(electrons/2))
    count = 1
    result = []
    for item in range(chislo_obolochek):
        if electrons > 2*(count**2):
            result.append(2*(count**2))
            electrons = electrons - 2*(count**2)
        else:
            result.append(electrons)
            return result
        count += 1
    return result