#!/usr/bin/python

def answer(pegs):
    # your code here
    n = len(pegs)
    rad = list()
    for index in range(n - 1):
        rad.insert(index + 1, pegs[index+1] - pegs[index])
    rad.insert(0, 0)
    
    num = -1 * rad[n-1]
    for index in range(n-1):
        num += rad[index]
    num *= 2
    den = 2 * n - 5 
    
    if num < 0 or den <=0 or den > num:
        return [-1, -1]
    else:
        x = 2
        while(x <= num and x <= den):
            if num % x == 0 and den % x == 0:
                num = num / x
                den = den / x
            x += 1        
        return [num, den]

pegs = [4, 30, 50]
print answer(pegs)
