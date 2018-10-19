# Segment Tree (Sum of given range)

## Description
Segment Tree is a basically a binary tree used for storing the intervals or segments. Each node in the Segment Tree represents an interval.
## Implementation
Since a Segment Tree is a binary tree, a simple linear array can be used to represent the Segment Tree. 
A Segment Tree can be built using recursion (bottom-up approach ).
Following is the implementation of segment tree. The program implements construction of segment tree for any given array. It also implements query operation.

## Code

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

    # Print whole segment tree
    printTree(1)
    print()
    # outputs 36, 9, 4, 1, 3, 5, 27, 16, 7, 9, 11,

    # Print sum of values in array from index 1 to 3 
    print("Sum of values in given range = ", getSum(1, 0, 5, 1, 3))
    # Outputs 15

    # Print sum of values in array from index 2 to 5 
    print("Sum of values in given range = ", getSum(1, 0, 5, 2, 5))
    # outputs 32

__Time Complexity: O(N)__