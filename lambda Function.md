### What are Lambda Functions ?
In Python, Anonymous function is a function that is defined without a name.
These Anonymous functions are called lambda functions

## Syntax of Lambda Function in python.
```
  lambda arguments: expression
```
## Example:
```
    # To Cube a number.
    cube = lambda x: x**3

    print(cube(10)) #output: 1000

    # To print the square of all the numbers in a list.

    my_list = [1, 2, 3, 4]

    square = lambda x: x**2

    print(list(map(square, my_list))) # output: [1, 4, 9, 16]
```
