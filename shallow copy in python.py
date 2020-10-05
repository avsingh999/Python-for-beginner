# You can find output of this Program in shallow copy in python.md
# importing "copy" for copy operations 
import copy 
  
# initializing list 1 
list1 = [10, 20, 30, [40, 50], 60] 
  
# using copy to shallow copy (List 2) 
list2 = copy.copy(list1) 
  
# original elements of list  (List 1)
print ("Original elements before shallow copying List 1") 
for i in range(0,len(list1)): 
  print (list1[i],end=" ") 
  
print("\r") 
  
# adding and element to new list  (List 2)
list2[3][0] = 70

# The new list of elements after deep copying (List 2)
print ("New list of elements after shallow copying List 2") 
for i in range(0,len( list1)): 
  print (list2[i],end=" ") 
  
print("\r") 
  
# checking if change is reflected 
"""
  It makes a copy of the reference to list 1 into list 2. 
  Think about it as a copy of list 1's Address. 
  So, the addresses of list 1 and list 2 will be the same i.e. they will be pointing to the same memory location.
"""

print ("Original elements after shallow copying List 1") 
for i in range(0,len( list1)): 
  print (list1[i],end=" ")
