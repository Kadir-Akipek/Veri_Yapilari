#bir fonksiyonun kendi içinde tekrar çağırılmasıdır

def calculateFactorial(num):
    #edge case(uç nokta, uç örnek) or exit condition(çıkış durumu)
    if num == 0:
        return 1
    else:
        return num * calculateFactorial(num - 1)

calculateFactorial(6)

def calculateContigiousSum(num):
    if num == 0:
        return 0
    else: 
        return num + sum(num - 1)

calculateContigiousSum(7)