# Read file in Python

## To read the data

```python
file=open("filename","r")
data=file.read()
```

## Using this method you can read encoded files and save the file data in list

```python
with open("enter your file_name","r",encoding='UTF8') as title:
        title=title.readlines() 
```

## To write a file in python

```python
file=open("filename","w")
file.write("Enter your data that needs to be written in the file")
```

## Another method to write in a file

```python
with open("file_name", "w") as f:
   f.write("data")
```
