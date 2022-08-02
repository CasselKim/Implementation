from decorator import playtime

@playtime
def heapSort(arr) : 
    print("heap sort : ",end='')
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr

def heapify(arr, now, size) : 
    max = now
    left=2*now+1
    right=2*now+2

    if left<size and arr[left]>arr[max] : 
        max=left
    if right<size and arr[right]>arr[max] : 
        max=right
    
    if now!=max : 
        arr[max], arr[now] = arr[now], arr[max]
        heapify(arr, max, size)

    