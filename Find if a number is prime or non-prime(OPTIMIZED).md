A number is said to be prime if its only factors are 1 and the number itself. The code is an optimized approach to find the number is prime or not.
``` python
def isPrime(number):
    if number <= 1: #Flags if number is less than or equal to 1
        return False
    if number <= 3: #2 and 3 are prime numbers
        return True
    if ((number % 2 == 0) or (number % 3 == 0)): #checks for multiples of 2 and 3
        return False
    i = 5
    while (i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return False
        i = i + 6
    return True



```
