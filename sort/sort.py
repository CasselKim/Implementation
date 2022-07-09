from typing import List
import random

def isSorted(array) :
    for i in range(1,len(array)) : 
        if array[i-1]>array[i] : 
            return False
    return True
    
array_normal = [random.randint(1,1000) for _ in range(1000)]
array_best = [i for i in range(1000)]
array_worst = [i for i in range(1000,-1,-1)]
tcs = [array_normal, array_best, array_worst]