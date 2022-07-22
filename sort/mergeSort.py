from decorator import playtime

@playtime
def mergeSort(array) : 

    if len(array)<=1 : 
        return array
    
    l,r = 0, len(array)
    m = len(array)//2

    res = []
    arr1 = mergeSort(array[l:m])[::-1]
    arr2 = mergeSort(array[m:r])[::-1]
    while arr1 and arr2 : 
        if arr1[-1]<arr2[-1] : 
            res.append(arr1.pop())
        else : 
            res.append(arr2.pop())
    while arr1 : 
        res.append(arr1.pop())
    while arr2 : 
        res.append(arr2.pop())
    
    return res