# Read file in Python

## To read the data

```
file=open("filename","r")
data=file.read()
```

## Using this method you can read encoded files and save the file data in list
```with open("enter your file_name","r",encoding='UTF8') as title:
        title=title.readlines() 
```

## To write a file in python

```
file=open("filename","w")
file.write("Enter your data that needs to be written in the file")
```
## Another method to write in a file
```
with open("file_name", "w") as f:
   f.write("data")
```
