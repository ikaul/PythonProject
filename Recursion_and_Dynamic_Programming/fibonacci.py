#!/usr/bin/python
class Fibonacci():
    def __init__(self):
        self.memo = dict()
        self.memo[0] = 1
        self.memo[1] = 1

    def next(self, num):
        if num > 1:
            self.memo[num] = self.next(num-1) + self.next(num-2)
        return self.memo[num]

f = Fibonacci()
for i in range(10):
    print f.next(i)
