## 숫자들 `0, 1, 2, 3, 4` 출력하기

```python
for x in range(5):
   print(x)
```

## `3, 4, 5` 출력하기

```python
for x in range(3, 6):
    print(x)
```

## `3, 5, 7` 출력하기

```python
for x in range(3, 8, 2):
    print(x)
```
    
## 예시

- List에 저장된 모든 숫자의 합을 찾는 프로그램

- 숫자들의 List

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
```
- 합계를 저장하기 위한 변수

```python
sum = 0
```

- List를 반복

```python
for val in numbers:
   sum = sum+val
```
- 결과: 합계는 `48`

```python
print("합계는", sum)
```
