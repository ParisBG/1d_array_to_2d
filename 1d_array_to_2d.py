#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:23:28 2022
@author: parisbg
"""

import numpy as np


original = [100,200,300,400]

m = 2
n = 2
#my_arr = [[1,2,3],[4,5,6],[7,8,9]]
#arr = [2][2]
#reshape any 1d array to a 2d array
#final = np.array(original).reshape(row,col)

def printMatrix(some_array):
    for row in some_array:
        for col in row:
            print(col, end=' ')
        print()
    print()
           
 
test = [ [] for _ in range(m) ]
   
for i in range(m):
    for j in range(n):
        x  = original.pop(0)
        print(x)
        test[i][j] = original.pop(0)
        

print(test)
#printMatrix(test)  


'''
printMatrix()
#arr.insert(2, ['a', 'b', 'c'])
arr.insert(2, [11, 12, 13])
printMatrix()
arr[1].insert(2,12)
printMatrix()
arr[2][0] = 10
printMatrix()
arr[0] = [100,200,300]
printMatrix()
del(arr[3])
printMatrix()
del(arr[1][2])
printMatrix()
arr[0] = [1,2,3]
printMatrix()
arr[2][1] = 11
printMatrix()
'''

#Formula to calculate address of a 2d array element 
#Address(arr[i][j]) = B + (i * C + j) * size


