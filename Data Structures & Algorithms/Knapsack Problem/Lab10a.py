# Brandon Gurley
# 11-14-2022
# CIS 360
# Lab 10

# n = number of items
# W = total allowed weight
# Profits = a list of n item Profits
# Weights = a list of n item Weights

import numpy as np


def knapsackDynamic(n, W, Profits, Weights):

    P = np.zeros((n+1, W+1), dtype = int)

    for w in range(0,W):
        P[0][w] = 0

    for i in range (1, n):
        P[i][0] = 0

    for i in range (1, n+1):
        for w in range(1, W+1):
            if Weights[i-1] <= w:
                profit_include = Profits[i-1] + P[i-1][w - Weights[i-1]]
                profit_omit = P[i-1][w]
                P[i][w] = max(profit_include, profit_omit)
            else:
                P[i][w] = P[i-1][w]
    return P

Profits = [20,30, 35]
Weights = [7,3,1]
W = 8
n = len(Profits)

print(knapsackDynamic(n, W, Profits, Weights))
