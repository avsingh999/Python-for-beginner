def get_input():
    num = int(input("Enter the number of fibonacci numbers you want"))
    return num


def fibonacci():
    number = get_input()
    a = 0
    b = 1
    if number == 1:
        print(b)
    elif number == 2:
        print(b, b)
    elif number > 2:
        for i in range(0, number):
            print(b)
            a = a+b
            print(a)
            b = a+b
    else:
        print("wrong input")


fibonacci()