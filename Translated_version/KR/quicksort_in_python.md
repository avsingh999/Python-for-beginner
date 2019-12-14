# QuickSort 알고리즘
## 설명 :

파이썬에서 [17,41,5,22,54,6,29,3,13] 형식으로 9개의 정수 목록 정렬하기

1. pivot을 찾습니다. pivot은 숫자2를 비교하는데 사용한 항목이므로 각 숫자를 차례로 pivot과 비교합니다. 작은 숫자값은 pivot의 왼쪽에 있고 큰 숫자값은 pivot의 오른쪽에 있습니다. pivot을 찾기 위해 3의 중앙값을 사용합니다. 첫번째값 (17), 중간값(54) 및 마지막값(13)을 선택합니다. 따라서 17은 이 세 값의 중앙값입니다.
2. pivot 값을 첫 번째 위치 (0 번째 위치)로 이동
3. 비교를 시작하십시오. 경계 값(41)을 갖습니다. 테두리보다 작은경우마다 현재 숫자값을 테두리값으로 바꿉니다. 따라서 pivot보다 작은 모든 숫자는 테두리 왼쪽에 있고 pivot보다 큰 숫자는 테두리 오른쪽에 있습니다.
4. 경계값(13)이 있는 위치로 17을 swap합니다. 따라서 이제 pivot 번호가 중간에 있습니다.
5. 위의 명령처럼 pivot보다 작은 숫자에 대해서는 quick sort를 수행하십시오.
6. 위의 명령처럼 pivot보다 큰 숫자에 대해서는 quick sort를 수행하십시오.

## 요약 :
. QuickSort는 재귀적입니다 (자신을 호출하는 메소드)
. 분할-정복 알고리즘
. 대용량 데이터세트에 매우 효율적
. 평균 case는 O(n log n)입니다.
. 성능은 주로 피벗 선택에 따라 다릅니다.

## 코드 :

### 사용자 input(D)을 나열한다음 재귀적으로 quick-sort2를 호출합니다.

```python
def quick_sort(D) :
	quick_sort2(D, 0, len(D) - 1)
```

```python
### 재귀적 함수
def quick_sort2 (D, low, high):
	if low < high:    #more than one item to be sorted
		p = partition(D, low, high)     # return the pivot around which where we partitioned the list
		quick_sort2(D, low, p - 1)      # sort left partition
		quick_sort2(D, p + 1, high)     # sort right partition
```

```python
### pivot을 얻기
def get_pivot(D, low, high):
	mid = (high + low) // 2
	pivot = high
	if D[low] < D[mid]:
		if D[mid] < D[high]:
			pivot = mid
	elif D[low] < D[high]:
		pivot = low
	return pivot
```

```python
### partition 함수
def partition(D, low, high):
	pivotIndex = get_pivot(D, low, high)
	pivotValue = D[pivotIndex]
	D[pivotIndex], D[low] = D[low], D[pivotIndex]   # swap the pivot value into the leftmost position of our list
	border = low                                    # set border to the lowest item 

	for i in range(low, high + 1):
		if D[i]  <  pivotValue:
		border += 1
		D[i], D[border] = D[border], D[i]
	D[low], D[border] = D[border], D[low]

	return (border)     # return the index for the pivot
```
