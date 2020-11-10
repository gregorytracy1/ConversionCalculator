userConverstionType = input("1: inches to mm. 2: or mm to inches")

converstionTypeInt = int(userConverstionType)
userNumber = input("Enter number: ")
userNumberFloat = float(userNumber)
# 1 would convert in to mm
if converstionTypeInt == 1:
    print("Convert inches to mm.")
    # 1 in = 25.4 mm
    # Convert from in to mm
    # userNumber * 25.4 mm = converted number
    convertedNumber = userNumberFloat * 25.4
    convertedString = "{0:.4f} inches is = {1:.4f} mm"

# 2 convert mm to in
if converstionTypeInt == 2:
    print("Convert mm to inches")
    # 25.4 mm = 1 in
    # Convert from mm to in
    # userNumber / 25.4 mm = converted number
    convertedNumber = userNumberFloat / 25.4
    convertedString = "{0:.4f} mm is = {1:.4f} inches"



print (convertedString.format(userNumberFloat, convertedNumber))