import math


def meet__user():
    messageForUser = "Hello user, this progam you helped find arithmetic average integer number or\ngeometric integer average number for two integer numbers\n";
    print(messageForUser)
    return 1


def info__choose__user():
    operationChooseUser = "\nEnter 1 for find arithmetic average number\nEnter 2 for find geometric average number"
    print(operationChooseUser)
    return 1


def input__user():
    userNum = int(input())
    return userNum


def arithmetic__average(num_1, num_2):
    result = (num_1 + num_2) / 2
    return result


def geometric__average(num_1, num_2):
    result = num_1 * num_2
    resultForUser = math.sqrt(result)
    return resultForUser


meet__user()
exitForProgram = 1
while (exitForProgram == 1):
    if exitForProgram == 1:
        info__choose__user()
        userOperation = input__user()
        if userOperation == 1:
            print("Enter you integer number 1")
            userNum_1 = input__user()

            print("Enter you integer number 2")
            userNum_2 = input__user()
            result = arithmetic__average(userNum_1, userNum_2)
            resultFormat = "{:.3f}".format(result)

            print("Arithmetic average --> " + str(resultFormat))
            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
        elif userOperation == 2:
            print("Enter you integer number 1 --> ")
            userNum_1 = input__user()

            print("Enter you integer number 2 --> ")
            userNum_2 = input__user()

            result = geometric__average(userNum_1, userNum_2)
            resultFormat = "{:.3f}".format(result)

            print("Geometric average --> " + (resultFormat))
            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
        else:
            print("Enter please 1 or 2, retry again")
            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
    else:
        exit()
