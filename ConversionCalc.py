# userConverstionType = input("1: inches to mm. 2: or mm to inches. Q to quit. ")

# converstionTypeInt = int(userConverstionType)
# userNumber = input("Enter number: ")
# userNumberFloat = float(userNumber)
# 1 would convert in to mm

# TODO loop to be able to process multiple calculations
# TODO add function to improve DRY concepts

# loop to continue until user selects Q
def print_calculation(con_string): # no parameters. Go inside ()
    print('Your answer is: ', con_string)

while True:
    # get menu selection from user
    userConverstionType = input("1: inches to mm. 2: or mm to inches. Q to quit. ")
    # prior to conversion, exit while loop
    if userConverstionType.isdigit() != True:
    # if the user input is string ---> error message go back to main menu
        if userConverstionType == 'Q':
            break
        print('That is not an option. Please choose from menu')
        continue # exit this iteration and continue in the next while loop iteration

    # converts user menu selection to an int
    converstionTypeInt = int(userConverstionType)

    # ask user number to convert
    userNumber = input("Enter number: ")

    # convert to a float for calc
    userNumberFloat = float(userNumber)

    if converstionTypeInt == 1:
        print("Convert inches to mm.")
        convertedNumber = userNumberFloat * 25.4
        convertedString = "{0:.4f} inches is = {1:.4f} mm"
        print_calculation(convertedString)

    # 2 convert mm to in
    # if converstionTypeInt == 2:
    #     print("Convert mm to inches")
    #     # 25.4 mm = 1 in
    #     # Convert from mm to in
    #     # userNumber / 25.4 mm = converted number
    #     convertedNumber = userNumberFloat / 25.4
    #     convertedString = "{0:.4f} mm is = {1:.4f} inches"
    

# print (convertedString.format(userNumberFloat, convertedNumber))