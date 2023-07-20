# Deque
# Çift Uçlu Queue' da diyebiliriz
# Deque yapısına baştan var sondan eleman ekleyebildiğimiz gibi baştan ve sondan eleman da kaldırabiliriz.

from collections import deque

myDeque = deque()
myDeque.append(10) # Deque yapısının sonuna eleman ekledik(10)
myDeque.append(20) # Deque yapısının sonuna eleman ekledik(20)
myDeque.appendleft(1) # Deque yapısının başına eleman ekledik(1)
myDeque.pop() # Deque yapısının son elemanını kaldırdık(20)
myDeque.popleft() # Deque yapısının ilk elemanını kaldırdık(1)
myDeque.pop() # Deque yapısının son elemanını kaldırdık(10)

