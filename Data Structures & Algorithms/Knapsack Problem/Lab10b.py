# Brandon Gurley
# 11-14-2022
# CIS 360
# Lab 10

# n = number of items
# W = total allowed weight
# Profits = a list of n item Profits
# Weights = a list of n item Weights

import numpy as np

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def knapackGreedy(W, array):
    sackvalue =0
    #sorts array based on ratio
    array.sort(key = lambda x: x.value/x.weight, reverse = True)
    for item in array:
        if item.weight <= W:
            W -= item.weight
            sackvalue += item.value

        else:
            sackvalue += item.value * W / item.weight
            break
    return sackvalue

if __name__ == "__main__":
    items = [Item(20,7), Item(30,3), Item(35,1)]
    print(items)
    W = 8
    n = len(items)
    print('Max Profit is: ')
    print(knapackGreedy(W, items))
