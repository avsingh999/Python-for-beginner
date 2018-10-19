# Segment Tree Implementation In Python

[Source - Hackerearth](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/)  

Segment Tree is used in cases where there are multiple range queries on array and modifications  
of elements of the same array.  

For example, finding the sum of all the elements in an array from indices *L to R*  
or finding the minimum (famously known as Range Minumum Query problem)  
of all the elements in an array from indices L to R.  

These problems can be easily solved with one of the most versatile data structures, Segment Tree.  

### What is Segment Tree ?  

Segment Tree is a basically a binary tree used for storing the intervals or segments.  
Each node in the Segment Tree represents an interval.  
Consider an array *A of size N* and a corresponding Segment Tree T:

The root of T will represent the whole array A[0:N−1].
Each leaf in the Segment Tree *T* will represent a single element *A[i]* such that *0 ≤ i < N*.  
The internal nodes in the Segment Tree T represents the union of elementary intervals A[i:j]  
where *0 ≤ i < j < N*.  

The root of the Segment Tree represents the whole array A[0:N−1].  
Then it is broken down into two half intervals or segments and the two children of the root in turn represent the 
A[0:(N−1)/2] and A[(N−1)/2+1 : (N−1)].  
So in each step, the segment is divided into half and the two children represent those two halves.  
So the height of the segment tree will be log<sub>2</sub>N.  

There are N leaves representing the N elements of the array.  
The number of internal nodes is N−1. So, a total number of nodes are 2N−1.

#### Segment tree provides two operations:
**Update** : To update the element of the array A and reflect the corresponding change in the Segment tree.  
**Query** : In this operation we can query on an interval or segment and return the answer to the problem  
(say minimum/maximum/summation in the particular segment).  

