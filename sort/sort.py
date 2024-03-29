from typing import List, Dict
from insertionSort import insertionSort, insertionSortBinarySearch, insertionSortBisect, linearSearch, binarySearch
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from mergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort
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

if __name__ == "__main__" :

    test_cases = createTestCases()
    
    for case_type,case in test_cases.items() : 

        print("case :",case_type)
        
        
        # Insertion Sort
        assert( isSorted(insertionSort(case.copy())) )
        assert( isSorted(insertionSortBinarySearch(case.copy())) )
        assert( isSorted(insertionSortBisect(case.copy())) )

        # Bubble Sort
        assert( isSorted(bubbleSort(case.copy())) )

        # Selection Sort
        assert( isSorted(selectionSort(case.copy())) )

        # Merge Sort
        assert( isSorted(mergeSort(case.copy())) )
        
        # Quick Sort
        assert( isSorted(quickSort(case.copy())) )

        # Heap Sort
        assert( isSorted(heapSort(case.copy())) )

        print()