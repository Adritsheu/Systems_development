from P3 import *
import matplotlib.pyplot as plt

naive = timeit(ns = (10, 20, 50, 100, 200, 500), pqclass = NaivePriorityQueue, n_average = 5)
myheap = timeit(ns = (10, 20, 50, 100, 200, 500), pqclass = HeapPriorityQueue, n_average = 5)
python = timeit(ns = (10, 20, 50, 100, 200, 500), pqclass = PythonHeapPriorityQueue, n_average = 5)

x = [10, 20, 50, 100, 200, 500]
plt.figure()
plt.title("Comparision of Running time of Merged Lists for 3 HeapPriority Queues")
plt.plot(x,naive, label = "Naive Priority Queue")
plt.plot(x,myheap, label = " My Min Heap Priority")
plt.plot(x,python, label = "Python Min Heap Priority")
plt.xlabel("Number of Lists Merged ")
plt.ylabel("Elapsed Time in seconds")
plt.legend()
plt.savefig("P3-C.png", dpi = 300, bbox_inches = 'tight')
plt.show()

