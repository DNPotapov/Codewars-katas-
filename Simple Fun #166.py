'''
Simple Fun #166: Best Match (5 kyu)
https://www.codewars.com/kata/58b38256e51f1c2af0000081/train/python
'''

def best_match(goals1, goals2):
    min_raznica = goals1[0] - goals2[0]
    res = 0
    for i in range(len(goals1)):
        if goals1[i] - goals2[i] < min_raznica:
            res = i
            min_raznica = goals1[i] - goals2[i]
        if (goals1[i] - goals2[i] == min_raznica) and (goals2[i] > goals2[res]):
            res = i
            min_raznica = goals1[i] - goals2[i]
    return res