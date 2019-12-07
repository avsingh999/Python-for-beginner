# 파이썬에서의 버블정렬

## 서술

버블정렬은 배열을 최소 n번 반복하고(n은 정렬할 배열요소의 수) 인접항목의 각 쌍을 비교하여 순서가 잘못된경우 교체한다.

__Worst Case 복잡도: n^2^__

## 코드

```python
# 정렬할 List
L = [5, 3, 2, 1, 6]

def bubble_sort(List):
	COMPLETED = False
	while not COMPLETED:
		COMPLETED = True
		for i in range(len(L) - 1):
			if List[i] > List[i+1]:
				COMPLETED = False
				List[i], List[i+1] = List[i+1], List[i]
	return List

print(bubble_sort(L))
```