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

# Function --> DRY
    #  some action is performed action repeated
    # def nameOfTheFunction(parameters1, parameters2, ...): # parameters are optional
        # Code for the function
        # return SomeDataType --> Optional
def convertINtoMM(inches):
    # this function converts in to mm 
    millimeters = float(inches) * 25.4
    return millimeters

def convertMMtoIN(mm):
    #this function converts mm to in
    inches = float(mm) / 25.4
    return inches
#print('The length of ' + userInches + 'in. is equal to ' + str(outputMM) + 'mm')
#print('The length of ' + userMM + 'mm is equal to ' + str(outputInches) + 'in')
def printResults(userInput, unitOfMeasuerment1, finalConversion, unitOfMeasuerment2):
    print('The length of ' 
    + userInput + unitOfMeasuerment1 
    + ' is equal to ' + str(finalConversion) +
    unitOfMeasuerment2)

while True:
    # Ask user
    userChoice = input('Please select: \n' 
                        '\t1.Inches to MM \n'
                        '\t2.MM to Inches \n'
                        '\tQ to Quit\n')
                        # If the user types quit --> Do the same thing as Q

    userChoice = userChoice.upper() # Change a user 'q' to 'Q'
    # Create a conditional statement
    if userChoice == '1':
        userInches = input('What are the inches? ') # this returns type str
        outputMM = convertINtoMM(userInches)
        printResults (userInches, 'in.', outputMM, 'mm')
    elif userChoice == '2':
        userMM = input('What are the mm? ') 
        outputInches = convertMMtoIN(userMM)
        printResults(userMM, 'mm', outputInches, 'in')
    elif userChoice[0] == 'Q': #
        break
    else:
        #This is anything that is not 1 or 2.
        print('That is not an option')





