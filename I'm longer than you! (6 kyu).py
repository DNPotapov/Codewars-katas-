'''
I'm longer than you! (6 kyu)
https://www.codewars.com/kata/5963314a51c68a26600000ae
'''

def longer(s):
    mass = {}
    for item in s.split():
        get_item = mass.get(len(item), [])
        mass[len(item)] = get_item + [item]
    res = []
    for i in sorted(mass):
        if len(mass[i]) > 1:
            res.extend(sorted(mass[i]))
        else:
            res.append(mass[i][0])
    return ' '.join(res)