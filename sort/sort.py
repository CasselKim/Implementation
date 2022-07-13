from typing import List, Dict
from insertionSort import insertionSort, insertionSortBinarySearch, insertionSortBisect, linearSearch, binarySearch
from bubbleSort import bubbleSort
from selectionSort import selectionSort
import random
import time

def isSorted(array:List[int]) -> bool :
    for i in range(1,len(array)) : 
        if array[i-1]>array[i] : 
            return False
    return True
    
def createTestCases() -> Dict[str,List[int]] : 
    array_normal = [random.randint(1,10000) for _ in range(10000)]
    array_best = [i for i in range(10000)]
    array_worst = [i for i in range(10000,-1,-1)]
    return {"array_normal":array_normal, "array_best":array_best, "array_worst":array_worst}

def checkTimeFrom() -> float : 
    return time.time()

def checkTimeTo(start:float,func_name:str) -> None: 
    print("{} conducting time : {}".format(func_name,time.time()-start))
    return 

if __name__ == "__main__" :

    test_cases = createTestCases()

    
    for case_type,case in test_cases.items() : 

        print("case :",case_type)
        
        # insertion sort
        start = checkTimeFrom()
        assert( isSorted(insertionSort(case)) )
        checkTimeTo(start,"insertionSort")
        start = checkTimeFrom()
        assert( isSorted(insertionSortBinarySearch(case)) )
        checkTimeTo(start,"insertionSortBinarySearch")
        start = checkTimeFrom()
        assert( isSorted(insertionSortBisect(case)) )
        checkTimeTo(start,"insertionSortBisect")

        start = checkTimeFrom()
        assert( isSorted(bubbleSort(case)) )
        checkTimeTo(start,"bubbleSort")

        start = checkTimeFrom()
        assert( isSorted(selectionSort(case)) )
        checkTimeTo(start,"bubbleSort")