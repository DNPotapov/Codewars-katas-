'''
Upper <body> Strength (7 kyu)
https://www.codewars.com/kata/571640812ad763313600132b
'''

def alex_mistakes(number_of_katas, time_limit):
    count = 0
    delay = 0
    time_doing = number_of_katas*6
    if time_doing == time_limit:
        return count
    while(time_doing + delay*2 <= time_limit):
        if count == 0:
            delay = 5
        else:
            delay = delay * 2
        time_doing += delay
        count += 1
    return count