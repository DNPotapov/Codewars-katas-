'''
Twice as old (8 kyu)
https://www.codewars.com/kata/5b853229cfde412a470000d0
'''

def twice_as_old(dad_years_old, son_years_old):
    if son_years_old == 0:
        return dad_years_old
    count = 0
    save_dad = dad_years_old
    while(dad_years_old/son_years_old != 2 and dad_years_old != 0):
        dad_years_old -= 1
        count += 1
    if dad_years_old != 0:
        return count
    else:
        count = 0
        while(save_dad/son_years_old != 2):
            save_dad += 1
            count += 1
        return count