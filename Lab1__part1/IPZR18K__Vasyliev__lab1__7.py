def meetUser():
    messageUser = "\nHello user.\nThis program checks your natural number to see if it is an even number or ended to 5 "
    print(messageUser)
    return 1


def inputNumInt():
    userNumInt = int(input())
    return userNumInt

def checkNaturalNumber():
    print("Enter your natural number please")
    userNaturalNum=inputNumInt()
    if userNaturalNum <= 0:
        print("Your number must be natural ( N > 0 )")
    elif userNaturalNum%2 == 0:
        print("Your number is even")
    elif userNaturalNum%5 == 0:
        if userNaturalNum%2 == 0:
            print("Your number is even")
        else:
            print("Your number ended to 5")
    else:
        print("You number is not even or ended to 5")
    return 1

def exitProgram(engineProgram):
    engineLoop = True
    while engineLoop == True:
        print("\nIf you want to retry enter 1.\nIf you want exit enter 0.\n")
        userChoose = inputNumInt()
        if userChoose == 1:
            engineProgram = True
            break
        elif userChoose == 0:
            engineProgram = False
            exit(0)
    return engineProgram


meetUser()
engineProgram = True
while engineProgram == True:
    checkNaturalNumber()
    exitProgram(engineProgram)
