from decorator import playtime

@playtime
def bubbleSort(array) : 
    print("bubble sort : ",end='')
    swap = True
    while swap : 
        swap = False
        for i in range(len(array)-1) : 
            if array[i]>array[i+1] : 
                array[i+1], array[i] = array[i], array[i+1]
                swap=True
    return array