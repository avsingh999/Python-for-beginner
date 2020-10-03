# You can find output of this Program in deep copy in python.md file
# importing "copy" for copy operations 

import copy 
  
# initializing list 1 
# You can choose your own desired input
list1 = [10, 20, 30, [40,50], 60,70] 
  
# using deepcopy to deep copy  
list2 = copy.deepcopy(list1) 
  
# original list items before  Deep Copying (List 1)
print ("Original list items before deep copying List 1") 
for i in range(0,len(list1)): 
  print (list1[i],end=" ") 
  
print("\r") 
  
# adding and item to the new list (list 2)
list2[3][0] = 80
  
# The new list of elements after deep copying (List 2)
print ("New list of elements after deep copying List 2") 
for i in range(0,len( list1)): 
  print (list2[i],end=" ") 
  
print("\r") 
  
# Change is NOT reflected in original list 1
""" 
  It makes a copy of all the members of List 1, 
  allocates different memory location for List 2 and then assigns the copied members to List 2 to achieve deep copy. 
  In this way, if List 1 vanishes List 2 is still valid in the memory.
"""
print ("Original elements after deep copying List 1") 
for i in range(0,len( list1)): 
  print (list1[i],end=" ") 