A number is said to be prime if its only factors are 1 and the number itself. The code is an optimized approach to find the number is prime or not.
``` python
def IsPrime(number):
    if number <= 1: #Flags if number is less than or equal to 1
        print("False")
        return
    if number <= 3: #2 and 3 are prime numbers
        print("True")
        return
    if ((number % 2 == 0) or (number % 3 == 0)): #checks for multiples of 2 and 3
        print("False")
        return
    i = 5
    while (i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            print("False")
            return
        i = i + 6
    print("True")
    return



```