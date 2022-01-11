from random import sample
from time import time
from P2 import MinHeap
import heapq
import numpy as np


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO


def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists):
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i))

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed




## Naive Priority
class NaivePriorityQueue(PriorityQueue):
    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError("Priority Queue is full")
        self.elements.append(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("This is an Empty Priority queue")
        small_val = self.peek()
        delete_ind = self.elements.index(small_val)
        self.elements.pop(delete_ind)
        return small_val
    
    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("This is an Empty priority queue")
        return min(self.elements)
    
## Heap Priority Class (mine)
class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.elements = MinHeap([]) # makes the elements a minheap class
        
        
    def put(self, val):
        if len(self.elements.elements) >= self.max_size:
            raise IndexError("Priority Queue is full")
        # use heap push
        self.elements.heappush(val)

    def get(self):
        if len(self.elements.elements) == 0:
            raise IndexError("This is an Empty Priority queue")
        # use heappop
        return self.elements.heappop()
    
    def peek(self):
        if len(self.elements.elements) == 0:
            raise IndexError("This is an Empty priority queue")
        return self.elements.elements[0] # should be sorted from heapify


        

## Python
class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
        heapq.heapify(self.elements) #how do i know if its a min vs max
        
    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError("Priority Queue is full")
        # use heap push
        heapq.heappush(self.elements, val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError("This is an Empty Priority queue")
        # use heappop
        return heapq.heappop(self.elements)
    
    def peek(self):
        if len(self.elements) == 0:
            raise IndexError("This is an Empty priority queue")
        return self.elements[0] # should be sorted from heapify
        
        

