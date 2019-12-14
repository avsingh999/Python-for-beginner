# 파이썬에서 segment 트리 구현

[출처- Hackerearth] (https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/)

segment 트리는 배열에 대해 여러 범위 쿼리가 있고 동일한 배열의 요소가 수정 된 경우에 사용됩니다.

예를 들어, 인덱스 *L부터 R까지* 배열의 모든요소의 합을 찾거나 인덱스 L에서 R로 배열의 모든요소의 최소값 (최소범위쿼리문제로 잘 알려져있음)을 찾는다고 해봅시다.

이러한 문제는 가장 다양한 데이터 구조 중 하나인 segment 트리를 사용하여 쉽게 해결할 수 있습니다.

### segment 트리 란 무엇입니까?

segment 트리는 기본적으로 간격 또는 segment를 저장하는데 사용되는 이진트리입니다.
segment 트리의 각 노드는 간격을 나타냅니다.
 *크기가 N인 A*배열과 해당 segment 트리 T를 고려하십시오.

T의 근은 전체 배열 A[0:N−1]을 나타냅니다.
segment 트리 *T*의 각 리프는 *0 ≤ i < N *가 되도록 단일 요소 *A[i]*를 나타냅니다.
segment 트리 T의 내부 노드는 기본 간격 A[i:j]의 합집합을 나타냅니다. 여기서 *0 ≤ i < j < N* 입니다.

segment 트리의 루트는 전체 배열 A[0:N−1]을 나타냅니다.
그런 다음 두 개의 반 간격 또는 segment로 분류되고 루트의 두 자식은 차례로 A[0:(N−1)/2] 및 A[(N−1)/2+1 : (N−1)] 을 나타냅니다.
따라서 각 단계에서 segment는 반으로 나뉘고 두 자녀는 그 두 반쪽을 나타냅니다.
따라서 segment 트리의 높이는 log<sub>2</sub>N이됩니다.

배열의 N 개 요소를 나타내는 N 개의 잎이 있습니다.
내부 노드의 수는 N-1입니다. 따라서 총 노드 수는 2N-1입니다

#### segment 트리는 두 가지 작업을 제공합니다.
** Update ** : 배열 A의 요소를 업데이트하고 segment 트리의 해당 변경 사항을 반영합니다.
** Query ** :이 작업에서는 구간 또는 segment를 쿼리하여 문제에 대한 답변을 반환 할 수 있습니다.
(특정 segment에서 최소 / 최대 / 합계).
<hr>
### 파이썬에서 segment 트리 구현

segment 트리는 이진 트리이기 때문에 간단한 선형 배열을 사용하여 segment 트리를 나타낼 수 있습니다.
segment 트리를 구축하기 전에 segment 트리의 노드에 무엇이 저장되어야하는지 파악해야합니다.
예를 들어, 인덱스 *L에서 R까지* 배열의 모든 요소의 합을 찾는것이 문제라면 각 노드 (리프 노드 제외)에서 하위노드의 합이 저장됩니다.

segment 트리는 재귀를 사용하여 구축 할 수 있습니다 (아래부터 위로 접근).
```
-> 리프에서 시작하여 루트로 이동하여 노드의 해당 변경사항을 업데이트하십시오.
-> 리프에서 루트까지의 경로에 있습니다.
-> 나뭇잎은 단일 요소를 나타냅니다.
-> 각 단계에서 두 개의 하위노드 데이터가 내부상위 노드를 형성하는데 사용됩니다.
-> 각 내부노드는 하위 간격의 합집합을 나타냅니다.
-> 질문마다 병합이 다를 수 있습니다.
-> 따라서 재귀는 전체배열을 나타내는 루트노드에서 끝납니다.
```  

For update(). 

```
-> 업데이트 할 요소가 포함된 리프를 검색하십시오.
-> 이것은 요소를 포함하는 간격에 따라 왼쪽자식이나 오른쪽자식으로 이동하여 수행할 수 있습니다.
-> 리프가 발견되면 리프가 업데이트되고 다시 상향식 접근 식을 사용하여 해당 리프에서 루트까지의 경로변경을 업데이트합니다.
```   

segment 트리에서 query()를 만들려면
```
-> L에서 R까지의 범위를 선택하십시오 (일반적으로 질문에 나와 있음).
-> 루트에서 시작하여 트리에서 되풀이하여 노드가 나타내는 간격이 L에서 R까지의 범위에 있는지 확인하십시오.
    노드가 나타내는 간격이 L에서 R까지의 범위에 있으면 해당 노드의 값을 반환합니다.
```  

크기가 7 인 배열 A의 segment 트리는 다음과 같습니다:  
![image](https://he-s3.s3.amazonaws.com/media/uploads/a0c7f90.jpg)   
![image](https://he-s3.s3.amazonaws.com/media/uploads/aad673e.jpg)   

**예시를 들어봅시다.**  크기가 N인 배열 A와 일부쿼리가 제공됩니다.
두가지 유형의 쿼리가 있습니다.
Update : idx 및 val이 주어지면 배열 요소 A[idx]를 A[idx] = A[idx]+val로 업데이트합니다.
Query : 주어진 l과 r은 0 ≤ l ≤ r <N이 되도록 A[l]+A[l+1]+A[l+2]+ … +A[r-1]+A[r]의 값을 반환
쿼리 및 업데이트는 어떤 순서로든 가능합니다.

*Naive 알고리즘*  
이것이 가장 기본적인 접근법입니다. 모든 쿼리에 대해 l에서 r까지 루프를 실행하고 모든요소의 합계를 계산하십시오.
따라서 각 쿼리는 O(N) 시간이 걸립니다.
A[idx] += val은 요소의 값을 업데이트합니다. 각 업데이트에는 O(1)가 걸립니다.

이 알고리즘은 배열의 업데이트에 비해 쿼리 수가 매우 적은경우에 좋습니다. 

*Segment 트리 사용하기:*  
먼저 segment 트리의 노드에 무엇이 저장되어야하는지 파악하십시오.
질문은 l에서 r까지의 간격으로 합산을 요청하므로 각 노드에서 해당간격의 모든요소의 합이 노드로 표시됩니다.
다음으로 segment 트리를 작성하십시오.
아래 주석이 포함 된 구현은 빌드 프로세스를 설명합니다

**segment 트리 building**  

```python
   def build(node, start, end):
       if start == end:
           tree[node] = A[start]    # 리프노드는 한개의 요소를 가지게될것
       else:
           mid = (start + end) / 2;
           build(2*node, start, mid)     # 왼쪽 자식에 재귀
           build(2*node+1, mid+1, end)  # 오른쪽 자식에 재귀 
           tree[node] = tree[2*node] + tree[2*node+1] # 내부 노드는 두 자식의 합계를 가짐
```   
**시간복잡도:** O(N)  
<hr>  

**segment 트리 Updating**  
```python
   def update(node, start, end, idx, val):
       if start == end:          # 리프 노드
           A[idx] += val
           tree[node] += val
       else:
           mid = (start + end) / 2;
           
           if start <= idx and idx <= mid:              # idx가 왼쪽 자식에 있으면 왼쪽 자식에 재귀
               update(2*node, start, mid, idx, val)
           else:                                        # idx가 올바른 자식을 갖는 경우 올바른 자식에 대해 재귀
               update(2*node+1, mid+1, end, idx, val)
               
           tree[node] = tree[2*node] + tree[2*node+1];  # 내부 노드는 두 자식의 합계를 가짐
```  
**시간복잡도:** O(logn)  
<hr>  

**segment 트리 Querying**  
```python
int query(int node, int start, int end, int l, int r)
{
    if(r < start or end < l)
    {
        // 노드가 나타내는 범위가 지정된 범위를 완전히 벗어남
        return 0;
    }
    if(l <= start and end <= r)
    {
        // 노드가 나타내는 범위는 주어진 범위 안에 완벽히 있음
        return tree[node];
    }
    // 노드로 표시되는 범위는 지정된 범위 내부 및 일부 범위를 벗어남
    int mid = (start + end) / 2;
    int p1 = query(2*node, start, mid, l, r);
    int p2 = query(2*node+1, mid+1, end, l, r);
    return (p1 + p2);
}
```

**시간복잡도:** O(logn)  








