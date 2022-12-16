"""
5x5 Nonogram Solver (4 kyu)
https://www.codewars.com//kata/5a479247e6be385a41000064
"""

import re
from itertools import product

class Nonogram:

    def __init__(self, clues):
        self.xclues = [list(c) for c in clues[0]]
        self.yclues = [list(c) for c in clues[1]]
        self.grid = [[0] * 5 for i in range(5)]
        self.perms = list(product([0, 1], repeat=5))

    def check(self, clue, house):
        ls = re.findall(r'[1]+', ''.join(house))
        if len(clue) != len(ls):
            return False
        for j, e in enumerate(clue):
            if len(ls[j]) != e:
                return False
        return True

    def valid(self):
        for i, r in enumerate(self.grid):
            if not self.check(self.yclues[i], map(str, r)):
                return False
        return True

    def lock(self, x, seq):
        for i, c in enumerate(seq):
            self.grid[i][x] = c

    def unlock(self, x):
        for i in range(5):
            self.grid[i][x] = 0

    def dfs(self, x):
        if x == 5:
            return self.valid()
        for perm in self.perms:
            self.lock(x, perm)
            if self.check(self.xclues[x], [str(self.grid[i][x]) for i in range(5)]):
                if self.dfs(x + 1):
                    return True
            self.unlock(x)
        return False

    def solve(self):
        self.dfs(0)
        return tuple(tuple(r) for r in self.grid)