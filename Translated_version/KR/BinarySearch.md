## 재귀적 이진탐색을 위한 파이썬 프로그램. 
  
### 있는경우엔 배열에서 `x` 변수를, 그 외에는 `-1` 반환 

```python
def binarySearch (arr, l, r, x): 
    # base case 체크
    if r >= l: 
        mid = l + (r - l)/2

        # 요소가 중간에 있는경우
        if arr[mid] == x: 
            return mid 

        # 요소가 중간보다 작으면 왼쪽 하위배열에만 존재할 수 있음  
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 

        # 그 외경우에 요소는 오른쪽 하위배열에만 존재할 수 있음
        else: 
            return binarySearch(arr, mid+1, r, x) 

    else: 
        # 요소가 배열안에 존재하지 않음
        return -1
```