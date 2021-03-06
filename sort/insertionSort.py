import bisect
from decorator import playtime

@playtime
def insertionSort(array) : 
    print("insertion sort : ",end='')
    res = []
    for i in range(len(array)) : 
        j = linearSearch(res,array[i])
        res.insert(j,array[i])
    return res

def bisect_left(arr, x, lo=0, hi=None) : 
    if lo < 0 :
        raise(Exception("io must be non-negative"))
    if hi is None : 
        hi = len(arr)
    while lo < hi : 
        mid = (lo+hi)//2
        if arr[mid] < x : 
            lo = mid+1
        else : 
            hi = mid
    return lo

def insort_left(arr, x, lo=0, hi=None) : 
    if lo < 0 :
        raise(Exception("lo must be non-negative"))
    if hi is None : 
        hi = len(arr)
    while lo<hi : 
        mid = (lo+hi)//2
        if arr[mid]<x : 
            lo = mid+1
        else : 
            hi = mid
    arr.insert(lo,x)

@playtime
def insertionSortBinarySearch(array) : 
    print("insertion sort (binary sort) : ",end='')
    res = []
    for i in range(len(array)) : 
        j = binarySearch(res,array[i])
        res.insert(j,array[i])
    return res

@playtime
def insertionSortBisect(array) : 
    print("insertion sort (bisect module) : ",end='')
    res = []
    for i in range(len(array)) : 
        j = bisect.bisect_left(res,array[i])
        res.insert(j,array[i])
    return res

def linearSearch(source,value) : 
    for i in range(len(source)) : 
        if source[i]>=value : 
            return i
    return len(source)

def binarySearch(source,value) : 
    return bisect_left(source,value)