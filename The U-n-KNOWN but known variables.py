'''
The U-n-KNOWN but known variables: Multiplication (6 kyu)
https://www.codewars.com/kata/571a8920b29485b065000582
'''

def the_var(the_variables):
    bykvi = {"a":13,"b":12,"c":11,"d":10,"e":9,"f":8,
             "g":7,"h":6,"i":5,"j":4,"k":3,"l":2,"m":1,
             "n":0,"o":1,"p":2,"q":3,"r":4,"s":5,"t":6,
             "u":7,"v":8,"w":9,"x":10,"y":11,"z":12}
    return bykvi[the_variables[0]] * bykvi[the_variables[2]]