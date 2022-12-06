'''
Equal Sides Of An Array (6 kyu)
https://www.codewars.com/kata/5679aa472b8f57fb8c000047
'''

def find_even_index(arr):
    for index, item in enumerate(arr):
        if sum(arr[index+1:]) == sum(arr[:index]):
            return index
    return -1