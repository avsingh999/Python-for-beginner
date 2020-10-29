# write a function that completes the following
# For multiples of 3, print "fizz"
# For multiples of 5, print "buzz"
# For multiple of both 3 and 5 print "FizzBuzz"

def fizzbuzz(n):
    for i in range (1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print (i, "- FizzBuzz")
        elif i % 5 == 0:
            print (i, "- buzz")
        elif i % 3 == 0:
            print (i, "- fizz")

fizzbuzz(20)
