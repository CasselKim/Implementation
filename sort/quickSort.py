from decorator import playtime

def divideConquer(array) : 
    if len(array) <= 1 : 
        return array
    
    pivot = array[len(array)//2]
    lower, equal, upper = [], [], []

    for x in array : 
        if x < pivot : 
            lower.append(x)
        elif x == pivot : 
            equal.append(x)
        else : 
            upper.append(x)
    return divideConquer(lower) + equal + divideConquer(upper)

@playtime
def quickSort(array) : 
    print("quick sort : ",end='')
    return divideConquer(array)

