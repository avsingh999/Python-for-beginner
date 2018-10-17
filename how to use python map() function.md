#Python map() function

##### map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)


#### Syntax

```
map(fun, iter)
```

#### Parameters :

```
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
```


## Example 

 Calculate the length of each word in the tuple:
 
 ```python
def myfunc(n):
  return len(n)



x = map(myfunc, ('apple', 'banana', 'cherry'))

print(list(x))
```

#### Output
[5, 6, 6]