
def romanEncoder(num):
    romans = {1:"I", 5: "V", 10: "X", 50: "L", 100: "C", 500:"D", 1000: "M"}
    oddRoman = {4:"IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
    asRoma = ""
    while(num > 0):
        if(num % 1000 == 0):
            asRoma += romans[1000]
        elif(num % 500 == 0):
            asRoma += romans[5]
        elif(num % 100 == 0):
            asRoma += romans[100]
        elif(num % 50 == 0):
            asRoma += romans[50]
        elif(num % 10 == 0):
            asRoma += romans[10]
        elif(num % 5 == 0):
            asRoma += romans[5]
        else:
            asRoma += romans[1]            
        num = num / 10

    return asRoma        