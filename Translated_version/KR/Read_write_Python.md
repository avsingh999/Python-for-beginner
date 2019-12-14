# 파이썬에서 파일 읽기

## 데이터를 읽는법

```python
file=open("filename","r")
data=file.read()
```

## 이 방법을 사용하면 인코딩 된 파일을 읽고 파일 데이터를 목록에 저장할 수 있습니다

```python
with open("enter your file_name","r",encoding='UTF8') as title:
        title=title.readlines() 
```

## 파일을 쓰는법

```python
file=open("filename","w")
file.write("Enter your data that needs to be written in the file")
```

## 파일을 쓰는 또 다른 방법

```python
with open("file_name", "w") as f:
   f.write("data")
```
