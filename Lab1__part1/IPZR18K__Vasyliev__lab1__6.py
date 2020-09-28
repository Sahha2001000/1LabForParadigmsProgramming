def meetUser():
    messageUser = "\nHello user.\nThis program help transform your hours, minutes, seconds (How on table clock) in degrees"
    print(messageUser)
    print("restrictions")
    print(" 0 <= hour <= 24")
    print(" 0 <= minutes <= 60")
    print(" 0 <= seconds <= 60\n")
    return 1


def inputNumInt():
    userNumInt = int(input())
    return userNumInt

def hoursToDegrees(userHour):
    #   1 hour == 30 degrees
    degreeHour = 30
    if userHour < 0:
        print("You number must be greater than zero")
    elif userHour <= 12:
        hoursDegrees = userHour*degreeHour
    elif  userHour > 12 and userHour < 24:
        hoursDegrees =  (userHour%12)*degreeHour
    elif hoursToDegrees == 24:
        hoursDegrees =  12*degreeHour
    elif hoursToDegrees > 24:
        print("Your hour greater than 24")
    else:
        print("ERROR")
        exit(1)
    return hoursDegrees

def minutesToDegrees(userMinutes):
    #   1 minutes == 30 / 60 = 0.5 degrees
    degreeMinutes = 0.5
    if userMinutes >= 0 or userMinutes <= 60:
        minutesDegrees = userMinutes*degreeMinutes
    elif userMinutes > 60:
        print("Enter please number from 0 to 60 ")
    else:
        print("ERROR")
        exit(1)
    return minutesDegrees

def secondsToDegrees(userSeconds):
    #   1 seconds == 30 / 3600 = 0.00833333333333333 degrees
    degreeSeconds = 0.00833333333333333
    if userSeconds >= 0 or userSeconds <= 60:
        secondsDegrees = userSeconds*degreeSeconds
    elif userSeconds >= 60:
        print("Enter please number from 0 to 60 ")
    else:
        print("ERROR")
        exit(1)
    return secondsDegrees


def outputTime(hours,minutes,seconds):
    if minutes == 60:
        minutes=0
    if seconds == 60:
        seconds = 0
    if hours>=0 and hours < 12:
        time = ("{0}:{1:=02}:{2:02}".format(hours,minutes,seconds))
        print(f"Your enter time : {time} a.m.")
    elif hours>=12 and hours <=23:
        time = ("{0}:{1:=02}:{2:02}".format(hours,minutes,seconds))
        print(f"Your enter time : {time} p.m.")
    else:
        print("ERROR")
        exit(1)
    return 1

def outputDegrees(hoursDegrees,minutesDegrees,secondsDegrees):
    print(f"Hours degrees : {hoursDegrees}")
    print(f"Minutes degrees : {minutesDegrees}")
    print(f"Seconds degrees : {secondsDegrees}")
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
    #input user
    print("Enter your hour:")
    userHour =inputNumInt()
    print("Enter your minutes:")
    userMinutes =inputNumInt()
    print("Enter your seconds:")
    userSeconds =inputNumInt()
    #output user time
    outputTime(userHour,userMinutes,userSeconds)
    #Transform to degrees
    degreesHour=hoursToDegrees(userHour)
    degreesMinutes=minutesToDegrees(userMinutes)
    degreesSeconds=secondsToDegrees(userSeconds)
    #output degrees
    outputDegrees(degreesHour,degreesMinutes,degreesSeconds)
    #exit program
    exitProgram(engineProgram)
