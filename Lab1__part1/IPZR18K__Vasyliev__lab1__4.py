def meetUser():
    messageUser = "\nHello user.\nThis program helped show reverse three-digit number, which you enter"
    print(messageUser)
    return 1


def inputNumInt():
    userNumInt = int(input())
    return userNumInt

def transformNumBackwards(userNum):
    userNumBackwards = 0
    while userNum > 0:
        # Залишив коментарі для кращого розуміння коду
        # знаходимо залишок - останню цифру за допомогою арифметичного оператора %
        # num = 123456789 % 10 || num = 9
        num = userNum % 10
        # ділимо націло - прибираємо останю цифру за допомогаю арифметичного опрератора //
        # num = 123456789 // 10 || userNum = 12345678
        userNum = userNum // 10
        # збільшуємо розрядність друого числа
        userNumBackwards = userNumBackwards * 10
        # додаємо до рзультату отриману цифру
        userNumBackwards = userNumBackwards + num
    return userNumBackwards

def isThreeDigit(userNum):
    if userNum >= 100 and userNum <= 999:
        print(f"You three-digit number, which you enter : {userNum}")
        transformUserNum = transformNumBackwards(userNum)
        print(f"You backwards three-digit number, which you enter : {transformUserNum}")
    elif userNum < 100 or userNum > 999 :
        print("Your number must be three-digit!")
        if userNum <= 0:
            print("Your number must be greater than zero!")
    else:
        print("Error")
        exit(1)
    return userNum

# тільки в 4 лабі зрозумів, як створити вихід з програми через функцію
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
    print("Enter you three-digit number : ")
    userNum = inputNumInt()
    isThreeDigit(userNum)
    exitProgram(engineProgram)
