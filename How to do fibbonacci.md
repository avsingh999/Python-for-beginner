# How to do fibonacci sequence

# Explanation

The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. Starting with `0` and `1`, the sequence goes `0, 1, 1, 2, 3, 5, 8, 13, 21, 34`, and so forth.

Written as a rule, the expression is `xn = xn-1 + xn-2`

# Example

This example of fibonacci takes a number as input and prints as many numbers as the user typed in.

```python
def fibonacci():
    myList = []
    cont = 0
    num = int(input("Please, insert a number: "))

    if num == 1:
        myList.append(1)
    elif num >= 2:
        myList.extend((1,1))
        while (num-2 != cont):
            myList.append(myList[-1]+myList[-2])
            cont+=1
    elif num <= 0:
        print("Error, number should start above 1")

    print(myList)

fibonacci()
```

The execution will be something like this:

```bash
py firstExercises/fibonacci.py
Please, enter a number: 4
[1, 1, 2, 3]
```
