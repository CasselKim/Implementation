from typing import List
from insertionSort import insertionSort, insertionSortBinarySearch
import random

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

if __name__ == "__main__" :

    test_cases = createTestCases()

    for case in test_cases : 
        # insertion sort
        assert( isSorted(insertionSort(case)) )
        assert( isSorted(insertionSortBinarySearch(case)) )