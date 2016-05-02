#!/usr/bin/python
def recursivePermutations(k, i):
    p = [[1], [2,1], [3,2,4,1], [6,3,7,2,5,4,8,1]]
    r = []

    for i in range(1,4):
        n = len(p[i])
	r.append( 2 * n + 1 - p[i])


    print r
recursivePermutations(10,10)
