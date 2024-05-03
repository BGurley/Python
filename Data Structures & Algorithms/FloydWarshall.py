#Brandon Gurley
#11-7-2022
#CIS 360
#Lab 9
import math
import numpy

def floyd2 (n, W, D, P):
    for i in range(0, n):
        for j in range(0, n):
            P[i][j] = -1
    D = W
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if(D[i][k] + D[k][j])<D[i][j]:
                    P[i][j] = k
                    D[i][j] = D[i][k] + D[k][j]

def path(q, r):
    if (P[q][r] != -1):
        path(q, P[q][r])
        print(P[q][r])
        path(P[q][r], r)

inf= (math.inf)

W = [[0,10,1,inf],[inf,0,inf,inf],[inf,inf, 0, 2],[inf, 3, inf, 0]]
P= numpy.zeros((4,4), dtype = int)
D = 0
floyd2(4, W, D, P)
print(W)
print(P)
path(0,1)
