# Requirements
#      Convert length (standard and metric)
#      Convert volume (standard and metric)
#      Convert temperature (Celsius and F)

# Scope Creep
#      Cool if the program had a GUI

# Refactoring
#       Make improvements to the code
#       How to make the code more efficient
#       DRY --> Don't Repeat Yourself

# Pseudo Code --> In our own words --> figuring out the logic of the program ---> Comments

# user input as to which conversion they want to do.

while True:
    # Ask user
    userChoice = input('Please select: \n' 
                        '\t1.Inches to MM \n'
                        '\t2.MM to Inches \n'
                        '\t12.MM to Inches \n'
                        '\tQ to Quit\n')
                        # If the user types quit --> Do the same thing as Q

    userChoice = userChoice.upper() # Change a user 'q' to 'Q'
    # Create a conditional statement
    if userChoice == '1':
        #conversion from in to mm
        # Convert inches into mm 
        # get the information from the user
        userInches = input('What are the inches? ') # this returns type str

        # Perform the conversion
        # 1 in = 25.4 mm
        outputMM = float(userInches) * 25.4

        # output the results to the user.
        # EX 1 in  --> The length of 1in. is equal to 25.4mm
        print('The length of ' + userInches + 'in. is equal to ' + str(outputMM) + 'mm')

    elif userChoice == '2':
        #conversion from mm to in
        # Convert mm to inches
        userMM = input('What are the mm? ')

        #Perform the conversion
        outputInches = float(userMM)/25.4

        #output to the user
        print('The length of ' + userMM + 'mm is equal to ' + str(outputInches) + 'in')
    elif userChoice[0] == 'Q': #
        break
    else:
        #This is anything that is not 1 or 2.
        print('That is not an option')




