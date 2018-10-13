## Quicksort algorithm in Python
### How does quicksort algorithm work?
Imagine you have the following array:
[2, 5, 7, 4, 1, 3, 9, 1] and you want to sort it.

Quicksort algorithm works this way:
1. Takes the first element of the array as a reference: The PIVOT.
2. Separates the other elements of the array in three groups: Equal to the pivot, more than the pivot, less than the pivot.<br>
So we would currently have:<br>
Pivot = 2<br>
equal = [] (empty)<br>
more = [5, 7, 4, 3, 9]<br>
less = [1, 1]<br>
3. Then, returns the three previously sorted arrays (recursion) joined: less + equal + more

Now let's see what it would look like in Python:
```[Python]
array = [2, 5, 7, 4, 1, 3, 9, 1]

def quicksort(array):
    if len(array) == 1:
        return array
    else:
        pivot = array[0]
        less_than = []
        equal = []
        more_than = []
        for i in array[1::]:
            if i == pivot:
                equal.append(i)
            if i > pivot:
                more_than.append(i)
            if i < pivot:
                less_than.append(i)
        return quicksort(less_than) + equal + quicksort(more_than)
```