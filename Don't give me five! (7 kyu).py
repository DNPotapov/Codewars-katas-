'''
Don't give me five! (7 kyu)
https://www.codewars.com/kata/5813d19765d81c592200001a
'''

def dont_give_me_five(start,end):
    mass = list(range(start,end+1))
    count = 0
    for item in mass:
        if "5" not in str(item):
            count += 1
    return count