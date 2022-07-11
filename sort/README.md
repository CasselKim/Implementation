# Sort Implementation
## Insertion Sort
```python
def insertionSort(array) : 
    res = []
    for i in range(len(array)) : 
        for j in range(len(res)) : 
            if array[i]<res[j] : 
                res.insert(j,array[i])
    return res
```
```python
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
            
    for i in range(len(array)) : 
        insort_left(res,array[i])
        
    return res
```
![image](insertionSort1.png)  
이진 탐색을 썼는데 그냥 했을 때 보다 느리다. 심지어 worst case일 때는 150배나 느린 것을 확인할 수 있다. 왜 그럴까?  
![image](insertionSort2.png)  
local method에서 global method로 바꿔봤다. 미묘하게 빨라지긴 했지만 여전히 linear search보다 느리다.
![image](insertionSort3.png)
bisect module로 돌려봤다. custom한 것 보다 빠를때도, 느릴때도 있다.
![image](insertionSort4.png)
linear search도 method로 만들어서 똑같은 조건 하에 테스트해보았더니 linear insertion이 더 느리게 나왔다. 함수 호출시간이 문제였나보다. 생각해보면 파라미터로 길이 1,000,000인 list를 stack에 계속 (나눠서) 넣어야 되니까 시간이 느렸던 것 같다.