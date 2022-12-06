'''
Getting MAD (6 kyu)
https://www.codewars.com/kata/593a061b942a27ac940000a7/train/python
'''

def getting_mad(arr):
    mass = []
    for item, index in enumerate(arr):
        for i, ind in enumerate(arr):
            if item != i:
                a = index - ind
                mass.append(abs(a))
    return min(mass, default=0)