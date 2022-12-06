'''
Land perimeter (5 kyu)
https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python
'''

def land_perimeter(grid):
    res = 0
    for i_l in range(len(grid)):
        for i_w in range(len(grid[0])):
            if grid[i_l][i_w] == 'X':
                res += 4
                if i_l < len(grid) - 1 and grid[i_l + 1][i_w] == 'X':
                    res -= 2
                if i_w < len(grid[0]) - 1 and grid[i_l][i_w + 1] == 'X':
                    res -= 2

    return f'Total land perimeter: {res}'