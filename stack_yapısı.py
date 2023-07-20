# Stack
# Listeye benzer ama son giren ilk çıkar kuralı vardır(LIFO)
# Stack' e eleman eklemek için Push
# Stack' ten eleman çıkartmak için Pop
# Top Stack' in üst kısmı, Base Stack' in alt kısmı

from queue import LifoQueue

lifoQueue = LifoQueue()
lifoQueue.put(1) # push işlemi yapıp Stack' e 1 elemanını ekledik
lifoQueue.put(10) # push işlemi yapıp Stack' e 10 elemanını ekledik
lifoQueue.put(20) # push işlemi yapıp Stack' e 20 elemanını ekledik
print(lifoQueue.get()) # pop işlemi yapıp Stack' teki son elemanı kaldırdık(20)
print(lifoQueue.get()) # pop işlemi yapıp Stack' teki son elemanı kaldırdık(10)
print(lifoQueue.get()) # pop işlemi yapıp Stack' teki son elemanı kaldırdık(1)