## 예시 1
- list에 저장되어있는 모든 숫자들의 합을 찾는 프로그램

- 숫자들의 list
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

- 합을 저장하기 위한 변수
sum = 0

- list을 반복
for val in numbers:
	sum = sum+val

- 출력: 합은 48
print("합은", sum)
