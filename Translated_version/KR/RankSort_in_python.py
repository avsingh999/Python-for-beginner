# ranksort
# 배열을 정렬하는 또 다른 방법
# 정수요소를 갖는 크기 N의 배열 A를 입력합니다.
# A의 요소를 A [0] <= A [1] <= A [2] <= .... <= A [n-1]로 재정렬합니다.

# 사용자가 어떤 크기든 배열A 입력 
A = [i for i in input().split()]
# N은 A의 길이입니다
N = len(A)
# 배열R은 배열A의 각 요소의 순위를 포함합니다.
R=[0 for i in range(N)]
for j in range(1,N):
    for i in range(j):
        if A[i] <= A[j]:
            R[j] = R[j] + 1
        else:
            R[i] = R[i] + 1
# 배열U는 배열R의 요소로 index를 갖는 배열A의 요소를 포함합니다.
# U는 A의 정렬된 배열입니다
U = [0 for i in range(N)]
for j in range(N):
    U[R[j]-1] = A[j]
# 정렬된 배열A를 얻습니다.
for j in range(N):
    A[j] = int(U[j])

print(A)
