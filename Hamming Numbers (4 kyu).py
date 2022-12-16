"""
Hamming Numbers (4 kyu)
https://www.codewars.com//kata/526d84b98f428f14a60008da
"""

def hamming(n):
    nums = [1]
    i, j, k = 0, 0, 0
    if n == 1:
        return 1
    else:
        for index in range(1, n):
            x = min(2 * nums[i], 3 * nums[j], 5 * nums[k])
            nums.append(x)
            if 2 * nums[i] <= x:
                i += 1
            if 3 * nums[j] <= x:
                j += 1
            if 5 * nums[k] <= x:
                k += 1
    return nums[len(nums) - 1]