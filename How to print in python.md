## Python print()

```python
print("Python")
```

## The full syntax of print() is:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

```  
## print() Parameters
##objects - object to the printed. * indicates that there may be more than one object
##sep - objects are separated by sep. Default value: ' '
##end - end is printed at last
##file - must be an object with write(string) method. If omitted it, sys.stdout will be used which prints objects on the screen.
##flush - If True, the stream is forcibly flushed. Default value: False
```

## Python print() with variable
There is multiple way to do it. One of them is using f-string.
```python
last_name = "Doe"
first_name = "John"
print(f"Hello. My name is {first_name} {last_name}.")
```
