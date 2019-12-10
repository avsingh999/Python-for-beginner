### Creating Variables

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

```python
x = 1.1
y = "Github"
print(x)
print(y)
```

Variables do not need to be declared with any particular type and can even change type after they have been set.

```python
x = 4           # x is of type int
x = "Facebook"  # x is now of type str
print(x)
```

### Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
Rules for Python variables:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)

> Remember that variables are case-sensitive

### Output Variables

The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

```python
x = "amazing"
print("Python is " + x)
```

You can also use the + character to add a variable to another variable:

```python
x = "Python is "
y = "amazing"
z =  x + y
print(z)
```

For numbers, the + character works as a mathematical operator:

```python
x = 5
y = 10
print(x + y)
```

If you try to combine a string and a number, Python will give you an error:

```python
x = 5
y = "Hello!"
print(x + y)
```
