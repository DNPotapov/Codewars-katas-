'''
Shifter words (7 kyu)
https://www.codewars.com/kata/603b2bb1c7646d000f900083
'''

def shifter(st):
    key = ["H", "I", "N", "O", "S", "X", "Z", "M", "W"]
    mass = st.split()
    count = 0
    result = 0
    check_dublicate = []
    for item in mass:
        for i in item:
            if i in key:
                count += 1
        if count == len(item) and item not in check_dublicate:
            result += 1
            check_dublicate.append(item)
        count = 0
    return result