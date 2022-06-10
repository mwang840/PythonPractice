import math
def romanEncoder(num):
    romans = {1:"I", 5: "V", 10: "X", 50: "L", 100: "C", 500:"D", 1000: "M", 5000: "G",
            10000: "H"}
    oddRoman = {4:"IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    asRoma = ""
    dividend = 1
    while (num > dividend):
        dividend*=10

    dividend /= 10

    while(dividend):
        trueDivide = int(num / dividend)
        if(trueDivide <= 3):
            asRoma += romans[dividend] * trueDivide
        elif(trueDivide == 4):
            asRoma += romans[dividend] + romans[dividend * 5]    
        elif(5 <= trueDivide <= 8):
            asRoma += romans[dividend * 5] + (romans[dividend] + trueDivide - 5)
        elif(trueDivide == 9):
            asRoma+= romans[dividend] + (romans[dividend * 10])
        num = math.floor(num % dividend)
        dividend /= 10    
                
    return asRoma        