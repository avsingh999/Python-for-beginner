height = int(input("Number of row: "))

for row in range(height):
    for col in range(7):
        if ((col == 0 or col == 6) and row != 0) or ((row == 0 or row == height//2) and (col > 0 and col < 6)):
            print("*", end="")
        else:
            print(end=" ")
    print()