# 파이썬에서 CSV 파일을 읽고 쓰는 방법

데이터 내보내기에 일반적으로 사용되는, CSV 파일은, 파이썬 표준 라이브러리를 사용하여 쉽게 읽거나 작성할 수 있습니다.

# 예시: CSV 파일에서 값 읽기
다음 프로그램은 여러줄에서 쉼표로 구분된 문자열을 포함하는 csv 파일의 내용을 읽습니다.

```python
import csv
with open('eggs.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(', '.join(row))
```

출력:
```bash
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam
```

# 예시: 2차원 list으로 CSV 파일 작성
다음 프로그램은 2차원 list의 문자열로 csv 파일을 만듭니다.

```python
import csv
output_list = [
    ['Spam', 'Spam', 'Spam', 'Spam', 'Spam', 'Baked Beans'],
    ['Spam', 'Lovely Spam', 'Wonderful Spam']
]
with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for row in output_list:
        spamwriter.writerow(row)
```

프로그램을 실행하면 `output_list` 의 값을 포함하는 csv 파일이 생성됩니다. 각 하위 목록은 한 줄에 해당합니다.