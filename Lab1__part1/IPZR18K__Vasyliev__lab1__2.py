
def meetUser():
    messageUser="\nHello user.\nThis program you helped changed place two integer number, which you enter  "
    print(messageUser)
    return 1
def inputUserInt():
    userNumInt= int(input())
    return userNumInt




meetUser()
engineProgram=True
while engineProgram==True:
    #userNumInt_1 = 10 || userNumInt_2 = 1
    print("Enter you first intger number : ")
    userNumInt_1 = inputUserInt()
    print("Enter you second intger number : ")
    userNumInt_2 =inputUserInt()
    print(f"Don't changed!\nFirst integer number : {userNumInt_1} || Second integer number : {userNumInt_2}")
    #userNumInt_1  = userNumInt_1+userNumInt_2 || userNumInt_1 = 10+1 || userNumInt_1 = 11
    userNumInt_1 = userNumInt_1 +userNumInt_2
    #userNumInt_2 = userNumInt_1 - userNumInt_2|| userNumInt_2= 11 -1 || userNumInt_2= 10
    userNumInt_2=userNumInt_1 -userNumInt_2
    # userNumInt_1 = userNumInt_1-userNumInt_2 || userNumInt_1= 11 - 10 || userNumInt_1= 1
    userNumInt_1 =userNumInt_1 -userNumInt_2
    print(f"Changed!\nFirst integer number : {userNumInt_1} || Second integer number : {userNumInt_2}")

    print("If you want retry enter your integer number for changed enter 1.\nIf you want exit program enter 0")
    exitProgram=inputUserInt()
    if exitProgram == 1:
        engineProgram=True
    elif exitProgram == 0:
        engineProgram= False
    else:
        print("Invalid number, restart program")
        exit()
