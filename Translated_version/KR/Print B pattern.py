for row in range(7):
    for col in range(7):
        if (col == 0) or (col == 6 and (row != 0 and row != 3 and row != 6)) or ((row == 0 or row == 3 or row == 6) and (col > 0 and col < 6)):
            print("*", end="")
        else:
            print(end=" ")
    print()