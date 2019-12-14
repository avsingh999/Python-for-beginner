# 병합정렬

## 묘사

개념적으로 병합 정렬은 다음과 같이 작동합니다.

1. 정렬되지 않은 목록을 각각 1 개의 요소를 포함하는 n 개의 하위 목록으로 나눕니다 (1 개의 요소 목록은 정렬 된 것으로 간주됨).
2. 하나의 하위목록만 남을 때까지 하위목록을 반복해서 병합하여 새로운 정렬된 하위 목록을 생성합니다. 정렬 된 목록이됩니다.

## Code

```python
def mergeSort(alist):
	print("Splitting ",alist)
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
```