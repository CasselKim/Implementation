from decorator import playtime

@playtime
def selectionSort(arr) : 
    print("selection sort : ",end='')
    for i in range(len(arr)) : 
        minimum = (arr[i], i)
        for j in range(i,len(arr)) : 
            if arr[j]<minimum[0] : 
                minimum=(arr[j],j)
        arr[i], arr[minimum[1]] = arr[minimum[1]], arr[i]
    return arr