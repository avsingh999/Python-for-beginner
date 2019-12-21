# 파이썬에서 주어진 1차원 배열의 주어진 범위에서의 합계를 찾으십시오.

```python
def find_sum_in_range(min_range, max_range, input_data):
    total_sum = 0
    for item in input_data:
        if min_range <= item <= max_range:
            total_sum += item
    return total_sum
```

출력은 다음과 같을것입니다:

#입력

```python
min_range = 0
max_range = 1000
input_data = [10, 20, 5, 99, -19, 8372, 7468]
```

# 출력

```python
find_sum_in_range(min_range, max_range, input_data)
```

```sh
134
```

## 복잡도

- 시간복잡도 - `O(n)`
- 공간복잡도 - `O(1)`
