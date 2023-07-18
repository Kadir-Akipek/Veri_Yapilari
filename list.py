#Dynamic List
import sys 

n = 15
myDynamicArray = []

for i in range(0,n):
    myLength = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    print(f"Length: {myLength} Byte: {myByte}")
    myDynamicArray.append(n)