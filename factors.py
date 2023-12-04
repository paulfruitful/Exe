weight = int(input("Weight: "))
unit = input("(k)g or (l)bs: ")
if unit.upper() == "k":
    converted = weight/0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight i kgs: " + str(converted))