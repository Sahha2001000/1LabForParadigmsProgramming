
def meet__user():
    messageForUser = "Hello user, in this program you show the capabilities of the output format Python\n";
    print(messageForUser)
    return 1

def inputUserInt():
    userNum = int(input())
    return userNum

def inputUserFloat():
    userNum = float(input())
    return userNum

def formatNumInt ():
    userNumInt=inputUserInt();
    resultFormatNumInt='%-3d'%userNumInt;
    return resultFormatNumInt

def formatNumFloat ():
    userNum=inputUserFloat()
    resultFormatNumFloat="{:10.10f}".format(userNum);
    return float(resultFormatNumFloat)

def formatNumFloatFixedDot(userNumFloat):
    formatFixedDot="{:<5.2f}".format(userNumFloat);
    return formatFixedDot

def formatLineString(userLineStr):
    formatLineStr="%.2s"%userLineStr
    return formatLineStr

meet__user()

engineProgram = True
while engineProgram == True:
    #int
    print("Enter you integer number(width space for number:3): ")
    userNumInt_1=formatNumInt()

    print("Enter you integer number(width space for number:3): ")
    userNumInt_2=formatNumInt()

    print("Enter you integer number(width space for number:3): ")
    userNumInt_3=formatNumInt()

    print("Enter you integer number(width space for number:3): ")
    userNumInt_4=formatNumInt()

    print(userNumInt_1,userNumInt_2,userNumInt_3,userNumInt_4,sep='||')

    #float
    print("Enter you float number(width space for number:10): ")
    userNumFloat_1=formatNumFloat()

    print("Enter you float number(width space for number:10): ")
    userNumFloat_2=formatNumFloat()

    print(f" First value for you float number : {userNumFloat_1}\nSecond value for you float number : {userNumFloat_2}")

    userNumFloatFixedDot_1=formatNumFloatFixedDot(userNumFloat_1)
    userNumFloatFixedDot_2=formatNumFloatFixedDot(userNumFloat_2)

    print(userNumFloatFixedDot_1,userNumFloatFixedDot_2, sep='||')

    #string
    userLineString=input("Enter you string line (width space for number:4): ")
    print('%.4s' %userLineString)

    #boolean
    print(f"Value logical(boolean) type: {engineProgram}")
    print("If you retry input for my program enter 1,\nif you want exit this program enter 0")
    userChoose=inputUserInt()
    if userChoose == 1:
        engineProgram=True
    elif userChoose == 0:
        engineProgram==False
    else:
        print("Invalid value")
        exit()



