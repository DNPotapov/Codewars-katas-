"""
Human readable duration format (4 kyu)
https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""

def format_duration(seconds):
    list_time = ["year", "day", "hour", "minute", "second"]
    y = 0
    d = 0
    h = 0
    m = 0
    s = 0
    result = ""
    if seconds == 0:
        return "now"
    while seconds > 0:
        if seconds >= 31536000:
            y += 1
            seconds -= 31536000
        else:
            if seconds >= 86400:
                d += 1
                seconds -= 86400
            else:
                if seconds >= 3600:
                    h += 1
                    seconds -= 3600
                else:
                    if seconds >= 60:
                        m += 1
                        seconds -= 60
                    else:
                        s = seconds
                        seconds -= seconds
    mass_time = [y,d,h,m,s]
    result = []
    for index,item in enumerate(mass_time):
        if item > 1 and index < 3:
            result.append(f"{item} {list_time[index]}s")
        else:
            if item > 1 and index == 3 and mass_time[4] > 0:
                result.append(f"{item} {list_time[index]}s")
            else:
                if item > 1:
                    result.append(f"{item} {list_time[index]}s")
                else:
                    if item > 0 and index < 3:
                        if item == 1:
                            result.append(f"{item} {list_time[index]}")
                    else:
                        if item > 0 and index == 3 and mass_time[4] > 0:
                            result.append(f"{item} {list_time[index]}")
                        else:
                            if item > 0:
                                result.append(f"{item} {list_time[index]}")
    if len(result) == 1:
        return result[0]
    else:
        if len(result) == 2:
            return f"{result[0]} and {result[1]}"
        else:
            return ", ".join(result[:-1]) + " and " + result[-1]