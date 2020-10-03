def is_prime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True  
n = int(input("Enter a number: "))
if(is_prime(n)):
    print(n)
else:
    while(is_prime(n)==0):
        n+=1
    print(n)


