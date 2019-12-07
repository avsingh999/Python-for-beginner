#ranksort 
#another method to sort the array
#input the array A of size N having integers elements.
#rearranges the elements of A such that A[0] <= A[1] <= A[2] <=....<= A[n-1] 

#user input array A of any size.
A = [i for i in input().split()]
# N is length of A
N = len(A)
# array R contain the rank of each element of array A
R=[0 for i in range(N)]
for j in range(1,N):
    for i in range(j):
        if A[i] <= A[j]:
            R[j] = R[j] + 1
        else:
            R[i] = R[i] + 1
# array U contains the elements of array A having index as the array R's elements
#U is the sorted array of A
U = [0 for i in range(N)]
for j in range(N):
    U[R[j]-1] = A[j]
# get the sorted array A
for j in range(N):
    A[j] = int(U[j])

print(A)
