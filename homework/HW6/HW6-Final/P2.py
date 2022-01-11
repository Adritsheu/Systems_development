from math import floor
from typing import List
import numpy as np

from math import floor
from typing import List
import numpy as np

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()


    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError

    def heapify(self, idx: int) -> None:
        # TODO: your solution from the previous question can go here
        #       but remember to use your new "self.compare(a, b)" instead
        #       of raw comparisons
        
        if idx >= self.size:
            return

            #getting parents index
        left = self.left(idx)
        right = self.right(idx)
        parent = self.parent(idx)
        minmax = np.copy(idx)
      
        # comparing size on left and with true size or current index
        if left < self.size and self.compare(self.elements[left],self.elements[minmax]):
            minmax = left

            
        #finding min and max values on each side
        if right < self.size and self.compare(self.elements[right],self.elements[minmax]):
            minmax = right

        if minmax != idx:
            self.swap(idx, minmax)
            self.heapify(idx)
    
    

    def build_heap(self) -> None:
         for i in range((self.size-1)//2, -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        def _help_heap(idx):
            current = self.elements[idx]
            parent = self.parent(idx)
            while self.compare(self.elements[idx], self.elements[parent]) and idx != 0:
                self.swap(idx, parent) # swapping the values
                idx = parent
                parent = self.parent(parent)
            self.elements[idx] = current
            
        self.elements.append(key)
        self.size += 1
        #need to do minus 1 because index starts at zero
        _help_heap((self.size-1))
        

    def heappop(self) -> int:
        if self.size == 0:
            raise IndexError("This is an empty heap")
        else:
            # change first and last
            self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
            deleted = self.elements[-1]
            self.elements.pop()
            self.size -= 1
            self.heapify(0)
            return deleted

    
    
class MinHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a < b
  
         

class MaxHeap(Heap):
    def compare(self, a: int, b: int) -> bool:
        return a > b # returns TRUE or FALSE






if __name__ == "__main__":
    mn = MinHeap([7,2,3,4,5,1])
    mx = MaxHeap([7,2,3,4,5,10])
    print(mn)
    # print(mx)
    # mn.heappush(6)
    # print(mn)
    # mx.heappop()
    print(mx)
