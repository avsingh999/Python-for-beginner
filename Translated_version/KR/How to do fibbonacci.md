# 피보나치 수열 하는법

# 설명

피보나치 수열은 숫자 그 바로 앞의 2개의 숫자를 더하여 숫자를 찾는 일련의 숫자들의 연속입니다.  `0` 과 `1` 로 시작하며, 순서는 `0, 1, 1, 2, 3, 5, 8, 13, 21, 34` 로, 쭉 이어집니다.

쓰여진 규칙대로, 표현식은  `xn = xn-1 + xn-2` 입니다.

# 예시

이 피보나치의 예시는 숫자 하나를 입력으로 받아서 사용자가 입력한 숫자만큼 숫자들을 출력합니다.

```python
def fibonacci():
    myList = []
    cont = 0
    num = int(input("숫자를 입력해주세요: "))

    if num == 1:
        myList.append(1)
    elif num >= 2:
        myList.extend((1,1))
        while (num-2 != cont):
            myList.append(myList[-1]+myList[-2])
            cont+=1
    elif num <= 0:
        print("에러, 숫자는 1보다 커야합니다.")

    print(myList)

fibonacci()
```

실행은 다음과 같을것ㅇ비니다.:

```bash
py firstExercises/fibonacci.py
숫자를 입력해주세요: 4
[1, 1, 2, 3]
```
