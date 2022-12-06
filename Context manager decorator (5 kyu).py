'''
Context manager decorator (5 kyu)
https://www.codewars.com/kata/54e0816286522e95990007de
'''

def contextmanager(func):
    def wrapper(*args, **kwargs):
        class Solution:
            def __init__(self, func, *args):
                self.obj = func(*args)

            def __enter__(self):
                return next(self.obj)

            def __exit__(self, *args):
                pass

        return Solution(func, *args)

    return wrapper