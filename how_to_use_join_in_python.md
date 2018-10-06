# How to Use join in Python
Join in Python has the format 
``string.join(sequence,[,sep])``

Where sep is a string separator used to concatenate elements of the
sequence which will be either a list or a tuple of strings.

The following function shows an example of a function that takes a 
sequence and seperator and concatenates them using **join** method

```
def joinSequenceSequence(sequence,sep):

    print(sep.join(sequence))
```

## Results

Calling the method as follows gives the result **1-2-3-4-5**
```
joinSequenceSequence(["1","2","3","4","5"],"-")
```
