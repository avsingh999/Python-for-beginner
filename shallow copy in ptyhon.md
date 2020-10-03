### Shallow Copy
Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object. If any of the fields of the object are references to other objects, just the reference addresses are copied, only the memory address is copied.

It makes a copy of the reference to X into Y. Think about it as a copy of X’s Address. So, the addresses of X and Y will be the same i.e. they will be pointing to the same memory location.

### Output
Original elements before shallow copying List 1                      
10 20 30 [40, 50] 60                                                 
New list of elements after shallow copying List 2                    
10 20 30 [70, 50] 60                                                 
Original elements after shallow copying List 1                       
10 20 30 [70, 50] 60 