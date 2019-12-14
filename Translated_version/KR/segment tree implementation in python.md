# Segment 트리 (주어진 범위의 합)

## 설명

Segment 트리는 기본적으로 간격 또는 Segment를 저장하는  사용되는 이진트리입니다. Segment 트리의 각 노드는 간격을 나타냅니다.

## 구현

Segment 트리는 이진트리이기 때문에 간단한 선형배열을 사용하여 Segment 트리를 나타낼 수 있습니다.
Segment 트리는 재귀를 사용하여 구축할 수 있습니다 (밑에서 위로 접근).
다음은 Segment 트리의 구현입니다. 이 프로그램은 주어진 배열에 대한 Segment 트리 구성을 구현합니다. 또한 쿼리 작업을 구현합니다.

## 코드
```python
	tree = [-1] * 100
    arr = [1, 3, 5, 7, 9, 11]

    def buildSegmentTree(node, start, end):
        if start == end:
            tree[node] = arr[start]
        
        else:
            mid = (start + end) // 2
            buildSegmentTree(2 * node, start, mid)
            buildSegmentTree((2 * node) + 1, mid+1, end)
            tree[node] = tree[2*node] + tree[(2*node) + 1]

    def printTree(node):
        if tree[node] == -1:
            return
        
        print(tree[node],end="")
        print(', ', end="")
        printTree(node * 2)
        printTree((node * 2) + 1)

    def getSum(node, start, end, qs, qe):
        if (qe < start or end < qs):
            return 0
        if (qs <= start and qe >= end):
            return tree[node]
        mid = (start + end) // 2
        partialSum1 = getSum(2 * node, start, mid, qs, qe)
        partialSum2 = getSum((2 * node) + 1, mid + 1, end, qs, qe)
        return (partialSum1 + partialSum2)

    buildSegmentTree(1, 0, 5)

    # 모든 Segment 트리 출력
    printTree(1)
    print()
    # 36, 9, 4, 1, 3, 5, 27, 16, 7, 9, 11, 출력

    # index 1에서 3까지 배열값들의 합을 인쇄  
    print("Sum of values in given range = ", getSum(1, 0, 5, 1, 3))
    # 15 출력

    # index 2에서 5까지 배열값들의 합을 인쇄 
    print("Sum of values in given range = ", getSum(1, 0, 5, 2, 5))
    # 32 출력
```

__Time Complexity: O(N)__