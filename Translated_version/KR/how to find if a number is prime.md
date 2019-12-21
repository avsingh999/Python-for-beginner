숫자의 유일한 인수가 1과 자기자신인경우 소수라고 합니다.
``` python
number = int(input())  # 키보드에서 입력을 받음
if number <= 1: #숫자가 1보다 작거나 같은 경우 지연
        print("False")
    
for factor in range (2,number): #2와 (숫자 -1) 사이의 인수들을 확인합니다.
  if (number % factor == 0):
    print("False")
print("True")


```
