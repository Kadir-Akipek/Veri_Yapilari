"""bir sorunu çözmeye çalışırken tüm 
yolları teker teker denemek zorunda kalabiliriz, bu tarz 
durumlarda işimizi kolaylaştırmak için yaptığımız
denemeleri bir yere kaydederiz"""

mylist = [5,10,15,5,20,15,5,10,5,100,10,20,15,100,5,10]

def fib(self, n: int) -> int:
    x,y = 0,1

    for i in range(n):
        x,y = y,x+y
        return x

memo = {}

def memoizationSolution(n):
    if n not in memo:
        memo[n] = fib(n)
    return memo[n]