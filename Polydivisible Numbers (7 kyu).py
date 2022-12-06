'''
Polydivisible Numbers (7 kyu)
https://www.codewars.com/kata/5e4217e476126b000170489b
'''

def polydivisible(x):
    count = 1
    mass = []
    for index,item in enumerate(str(x)):
        mass.append(item)
        chislo = int(''.join((str(i) for i in mass)))
        if chislo % count == 0:
            count += 1
        else:
            return False
    return True