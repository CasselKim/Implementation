# Sort Implementation
## Insertion Sort
### code
```python
def insertionSort(array) : 
    res = []
    for i in range(len(array)) : 
        j = linearSearch(res,array[i])
        res.insert(j,array[i])
    return res
```
```python
def insertionSortBinarySearch(array) : 
    res = []
    for i in range(len(array)) : 
        j = binarySearch(res,array[i])
        res.insert(j,array[i])
    return res
```
```python
def insertionSortBisect(array) : 
    res = []
    for i in range(len(array)) : 
        j = bisect.bisect_left(res,array[i])
        res.insert(j,array[i])
    return res
```
### result
![image](insertionSort.png)

## Bubble Sort
### code
```python
def bubbleSort(array) : 
    swap = True
    while swap : 
        swap = False
        for i in range(len(array)-1) : 
            if array[i]>array[i+1] : 
                array[i+1], array[i] = array[i], array[i+1]
                swap=True
    return array
```
### result
![image](bubbleSort.PNG)  
