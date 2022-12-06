'''
Maximum subarray sum (5 kyu)
https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
'''

def max_sequence(arr):
    max = 0
    cur = 0
    for x in arr:
        cur += x
        if cur < 0:
            cur = 0
        if cur > max:
            max = cur
    return max