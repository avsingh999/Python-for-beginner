import math

N=int(input("소수인지 찾을 값들을 입력하십시오."))
primeflag=[0 for i in range(N+1)]
for i in range(2,int(math.sqrt(N))+1):
    for j in range(i*i,N+1,i):
        primeflag[j]=1
primeflag[0]=1
primeflag[1]=1
for i in range(N):
    if primeflag[i]==0:
        print(str(i) + "는 소수입니다.")
