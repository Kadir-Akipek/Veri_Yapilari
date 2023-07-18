#Big(O) gösterimi her zaman en kötü senaryoyu düşünür.
#Time Complexity(Zaman Karmaşıklığı) yazılan algoritmanın çalışma süresi.
#Space Complexity(Alan Karmaşıklığı) yazılan algoritmanın bellekte tuttuğu yer.

# Big(O) Complexity Chart From Good to Bad
# O(1) - O(log n) - O(n) - O(n log n) - O(n^2) - O(2^n) - O(n!)

def bigon(n):
    for i in range(0,n):
        print(i)

bigon(5)

def bigon2(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)

bigon2(5)

def bigon3(n):
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                print(i,j,k)

bigon3(5)

import math

def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)

logn(64)

def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(1,lim):
            print(i)

nlogn(16)

def nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n-1) #recursive

#O(n)
counter = 0
def actualFactorial(n):
    global counter
    counter += 1
    print(counter)
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * actualFactorial(n-1))