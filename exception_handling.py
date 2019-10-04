# Exception Handling in Python

## What is exception handling?
Exception handling is the process of responding to exceptions when a computer program runs. An exception occurs when an unexpected event happens that requires special processing.

## Python exception handing:

The `try` block lets you test a block of code for errors.

The `except` block lets you handle the error.

The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

## How to use:
```
try:
  print(x)
except:
  print("An exception occurred")
```

## Example

without exception handling
```
>>> print( 0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

after exception handling
```
try:
  print( 0 / 0)
except ZeroDivisionError:
  print ("denominator can't be zero.")
finally:
  print ("you handled exception very well")
```

output of above code
```
denominator can't be zero.
you handled exception very well
```
