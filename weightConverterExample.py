weight = float(input("Enter weight: "))
unit = input("Is it in (K)g or (L)bs?: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print ("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print ("Weight in Kg: " + str(converted))