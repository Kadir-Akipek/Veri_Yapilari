# Queue
# Listeye benzer ama ilk giren ilk çıkar kuralı vardır(FIFO)
# Queue' ye eleman eklemek için Enqeueu
# Queue' den eleman kaldırmak için Dequeue
# Front Queue' nin ilk girenler kısmı, Rear sondan girenler kısmı

from queue import Queue

myQueue = Queue()
myQueue.put(1) # Enqueue işlemi yapıp Queue' ye 1 elemanını ekledik
myQueue.put(10) # Enqueue işlemi yapıp Queue' ye 10 elemanını ekledik
myQueue.put(20) # Enqueue işlemi yapıp Queue' ye 20 elemanını ekledik
myQueue.get() # Dequeue işlemi yapıp Queue' nun ilk elemanı kaldırdık(1)
myQueue.get() # Dequeue işlemi yapıp Queue' nun ilk elemanı kaldırdık(10)
myQueue.get() # Dequeue işlemi yapıp Queue' nun ilk elemanı kaldırdık(20)