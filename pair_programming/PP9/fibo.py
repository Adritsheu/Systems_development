import reprlib
class Fibonacci():
    def __init__(self,number):
        self.number = number
    
    def __iter__(self):
        return FibonacciIterator(self.number)

    # def __repr__(self):
    #     return "Fibonaccis (%s)" % reprlib.repr(self.number)


class FibonacciIterator():
    def __init__(self,number):
        self.number = number
        self.index = 0  # starting index
        self.previous = 0
        self.current = 1


    def __next__(self):
        temp = self.previous
        self.previous = self.current
        self.current = temp + self.current
        if self.index >= self.number:
            raise StopIteration() #when reaches the end
        self.index += 1
        return self.current

    def __iter__(self):
        #print("iter")
        return self


if __name__ == "__main__":
    fib = Fibonacci(10)
    print(fib)
    print(list(iter(fib)))

