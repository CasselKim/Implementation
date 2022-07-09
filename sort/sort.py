from typing import List
from insertionSort import insertionSort, insertionSortBinarySearch
import random
import time

def isSorted(array) :
    for i in range(1,len(array)) : 
        if array[i-1]>array[i] : 
            return False
    return True
    
def createTestCases() : 
    array_normal = [random.randint(1,1000) for _ in range(1000)]
    array_best = [i for i in range(1000)]
    array_worst = [i for i in range(1000,-1,-1)]
    return [array_normal, array_best, array_worst]

def checkTimeFrom() : 
    return time.time()

def checkTimeTo(start,func_name) : 
    print("{} conducting time : {}".format(func_name,time.time()-start))

if __name__ == "__main__" :

    test_cases = createTestCases()

    for case in test_cases : 
        # insertion sort
        start = checkTimeFrom()
        assert( isSorted(insertionSort(case)) )
        checkTimeTo(start,"insertionSort")
        start = checkTimeFrom()
        assert( isSorted(insertionSortBinarySearch(case)) )
        checkTimeTo(start,"insertionSortBinarySearch")