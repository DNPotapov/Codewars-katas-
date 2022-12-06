'''
Maximum Subarray Sum II (5 kyu)
https://www.codewars.com/kata/56e3cbb5a28956899400073f/train/python
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

def find_subarr_maxsum(arr):
    max_sum = max_sequence(arr)
    mass = []
    if not max_sum: return [[], max_sum]
    for i in range(len(arr) + 1):
        for j in range(len(arr) + 1):
            mass.append(arr[i:j])
    res = [x for x in filter(lambda x: sum(x) == max_sum, mass)]
    if len(res) < 2:
        res = [res[0]] + [max_sum]
    else:
        res = [res] + [max_sum]
    return res