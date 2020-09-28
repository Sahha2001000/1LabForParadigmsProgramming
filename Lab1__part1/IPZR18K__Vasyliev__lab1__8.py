def meetUser():
    messageUser = "\nHello user.\nThis program checks your number day thereafter show what  is day it in week "
    print(messageUser)
    print("\nrestrictions")
    print(" 1 <= number day <= 365")
    print("not a leap year!")
    return 1


def inputNumInt():
    userNumInt = int(input())
    return userNumInt

def checkNumberDay(userDayNum):
    if userDayNum <= 0:
        print("You must enter number day correct")
        print("Tip: number day > 0 !!!")
    elif userDayNum % 7 == 0:
        print("Sunday is today")
    elif userDayNum % 7 == 1:
        print("Monday is today")
    elif userDayNum % 7 == 2:
        print("Tuesday is today")
    elif userDayNum % 7 == 3:
        print("Wednesday is today")
    elif userDayNum % 7 == 4:
        print("Thursday is today")
    elif userDayNum % 7 == 5:
        print("Friday is today")
    elif userDayNum % 7 == 6:
        print("Saturday is today")
    else:
        print("Error")
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
    print("Enter your  number day please")
    userDay=inputNumInt()
    checkNumberDay(userDay)
    exitProgram(engineProgram)
