def insertionSort(array) : 
    res = []
    for i in range(len(array)) : 
        for j in range(len(res)) : 
            if array[i]<res[j] : 
                res.insert(j,array[i])
    return res

def insertionSortBinarySearch(array) : 
    res = []
    
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
            
    for x in array : 
        insort_left(res,x)
        
    return res