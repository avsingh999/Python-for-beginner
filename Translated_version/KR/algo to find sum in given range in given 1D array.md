# 주어진 1차원 배열에 대해 주어진 범위안에서의 합계를 찾는 알고리즘

1. arr이라 불리는 변수에 정수배열을 저장
2. 합계를 수행 할 범위를 입력
3. index라고 불리는 새로운 변수를 0으로 초기화
4. sum이라고 불리는 새로운 변수를 만들어 0을 할당
5. 변수 index가 정해진 범위보다 작은지 확인해보고, 참인 경우 6단계나 9단계로 이동
6. index번째 index와 변수 sum의 합계를 변수 sum에 할당
7. index를 1씩 증가
8. 5단계로 이동
9. sum의 값을 출력

## 코드:

```python
arr = [1, 2, 3, 4, 5]
range = 3
index = 0
sum = 0

while(index < range):
  sum = sum + arr[index]
  index = index + 1

print(sum) 
```
