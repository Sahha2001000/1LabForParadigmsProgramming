def meet__user():
    messageForUser = "Hello user, this progam you helped find the maximum and minimum value of two different fractional numbers.\n";
    print(messageForUser)
    return 1


def input__user():
    userNum = int(input())
    return userNum


def fraction(num_1, num_2):
    fractionUser = num_1 / num_2
    return fractionUser


meet__user()
exitForProgram = 1
while (exitForProgram == 1):
    if exitForProgram == 1:
        print("Enter top part for first fractiom")
        numTopFraction_1 = input__user()
        print("Enter bottom part for first fractiom")
        numBottomFraction_1 = input__user()

        print("Enter top part for second fractiom")
        numTopFraction_2 = input__user()
        print("Enter bottom part for second fractiom")
        numBottomFraction_2 = input__user()

        numFraction_1 = fraction(numTopFraction_1, numBottomFraction_1)
        numFraction_2 = fraction(numTopFraction_2, numBottomFraction_2)
        if numFraction_1 > numFraction_2:
            print("numFraction_1 > numFraction_2")
            numFraction_1f = str("{:.3f}".format(numFraction_1))
            numFraction_2f = str("{:.3f}".format(numFraction_2))

            print("First Fraction == MAX --> " + numFraction_1f + "\nSecond Fraction  == MIN --> " + numFraction_2f)
            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
        elif numFraction_1 < numFraction_2:
            print("numFraction_1 < numFraction_2")
            numFraction_1f = str("{:.3f}".format(numFraction_1))
            numFraction_2f = str("{:.3f}".format(numFraction_2))

            print("First Fraction == Min--> " + numFraction_1f + "\nSecond Fraction == MAX First -->" + numFraction_2f)

            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
        elif numFraction_1 == numFraction_2:
            print("numFraction_1 == numFraction_2")
            numFraction_1f = str("{:.3f}".format(numFraction_1))
            numFraction_2f = str("{:.3f}".format(numFraction_2))
            print("First Fraction --> " + numFraction_1f + " == Second Fraction --> " + numFraction_2f)

            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
        else:
            print("If you want exit this program enter any number else don't exit program enter 1 ")
            exitForProgram = input__user()
    else:
        exit()
