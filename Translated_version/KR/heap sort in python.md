# 힙 정렬

## 서술

힙정렬 알고리즘은 두 파트로 나눌 수 있습니다.

첫 단계에서, 데이터로 힙을 만듭니다. 힙은 종종 완전 이진트리의 레이아웃으로 배열에 배치됩니다. 완전 이진 트리는 이진 트리 구조를 배열 index들에 매핑합니다; 각 배열 index는 노드를 나타냅니다; 노드의 부모, 왼쪽 자식가지 또는 오른쪽 자식 가지의 index는 간단한 표현식입니다. 0부터 시작하는 배열의 경우, 뿌리 노트는 index 0에 저장됩니다; 만약 i가 현재 노드의 index일 경우, 

```python
iParent(i) = floor((i-1) / 2) # floor 함수들이 실수를 가장 작은 선행 정수로 매핑하는곳
iLeftChild(i) = 2*i + 1
iRightChild(i) = 2*i + 2
```

두번째 단계에서, 정렬된 배열은 힙(힙의 root)에서 가장 큰 요소를 반복적으로 제거하고 배열에 삽입하여 생성됩니다. 힙 등록정보를 유지보수하기위해 각 제거 후에 힙이 업데이트됩니다. 힙에서 모든 객체가 제거되면, 결과물은 정렬된 배열입니다.

힙정렬은 제자리에서 수행 될 수 있습니다. 배열은 정렬된 배열과 힙, 두 부분으로 나눌 수 있습니다. 여기에 배열로서의 힙의 저장하는 방법이 도식화되어있습니다. 힙의 불변량은 각 추출 후에도 유지되므로, 유일한 비용은 추출 비용입니다.

__최악의 경우 복잡도: n * log(n)__

## 코드
```python
def heapify(arr, n, i):
	# root와 자식중에서 가장 큰 것 찾기
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2 
	
	if l < n and arr[i] < arr[l]:
		largest = l
	
	if r < n and arr[largest] < arr[r]:
		largest = r
	
	# 루트가 가장 크지 않은경우, 가장 큰 root와 swap하고 힙화를 계속합니다.
	if largest != i:
		arr[i], arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest)
	
def heapSort(arr):
	n = len(arr)
	
	# max heap 생성
	for i in range(n, 0, -1):
		heapify(arr, n, i)
	
	
	for i in range(n-1, 0, -1):
		# swap
		arr[i], arr[0] = arr[0], arr[i]  
		
		#힙화 root 요소
		heapify(arr, i, 0)
	 

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("정렬된 배열은 이와 같습니다.")
for i in range(n):
	print ("%d" %arr[i])
```
