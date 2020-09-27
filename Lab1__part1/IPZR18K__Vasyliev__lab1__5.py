def meetUser():
    messageUser = "\nHello user.\nThis program help transform you seconds from start day in hours and minutes"
    print(messageUser)
    return 1


def inputNumInt():
    userNumInt = int(input())
    return userNumInt

def secondsToHours(seconds):
    #   1 hour == 3600 seconds
    #   seconds=82800 || hours =(82800//3600)%24 || 23 % 24 = 23
    hours = ((seconds//3600))%24
    return hours

def secondsToMinutes(seconds):
    #   1 minutes == 60 seconds
    #   seconds=82800 || min =(82800//60)%60 || 0 % 60 = 0
    minutes = (seconds//60)%60
    return minutes

def outputTime(hours,minutes):
    print("{0}:{1:=02}".format(hours,minutes))
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
    print("Enter seconds please")
    secondsUser = inputNumInt()
    # transofm
    hoursUser = secondsToHours(secondsUser)
    minutesUser=secondsToMinutes(secondsUser)
    # output
    outputTime(hoursUser,minutesUser)
    exitProgram(engineProgram)
