### Deep Copy
A deep copy copies all fields, and makes copies of dynamically allocated memory pointed to by the fields. A deep copy occurs when an object is copied along with the objects to which it refers.

It makes a copy of all the members of X, allocates different memory location for Y and then assigns the copied members to Y to achieve deep copy. In this way, if X vanishes Y is still valid in the memory.

### Output
Original list items before deep copying List 1                       
10 20 30 [40, 50] 60 70                                              
New list of elements after deep copying List 2                       
10 20 30 [80, 50] 60 70                                              
Original elements after deep copying List 1                          
10 20 30 [40, 50] 60 70