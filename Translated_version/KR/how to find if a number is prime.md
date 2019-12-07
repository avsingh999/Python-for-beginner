A number is said to be prime if its only factors are 1 and the number itself
``` python
number = int(input())  # takes input from keyboard
if number <= 1: #Flags if number is less than or equal to 1
        print("False")
    
for factor in range (2,number): #checks for factors between 2 and the (number-1)
  if (number % factor == 0):
    print("False")
print("True")


```
