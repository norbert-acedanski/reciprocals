import sys

def calculateDecimalExpansion(number: int, printShortDescription: bool=True):
    if number < 2:
        print("Enter number greater than 1!")
        sys.exit()
    decimalExpansionList = []
    remainderList = []
    currentRemainder = 1
    # wholeDivisionProduct = 0
    periodIndex = -1
    while True:
        currentRemainder *= 10
        wholeDivisionProduct = currentRemainder // number
        currentRemainder %= number
        if wholeDivisionProduct in decimalExpansionList:
            indeces = [i for i, x in enumerate(decimalExpansionList) if x == wholeDivisionProduct]
            for i in indeces:
                if remainderList[i] == currentRemainder and currentRemainder != 0:
                    periodIndex = i
                    break
        if currentRemainder == 0:
            periodIndex = -1
            break
        elif periodIndex >= 0:
            break
        decimalExpansionList.append(wholeDivisionProduct)
        remainderList.append(currentRemainder)
    if currentRemainder == 0:
        if printShortDescription:
            print("Reciprocal of " + str(number) + " has no period.")
            print("1/" + str(number) + " = ", end="")
        print("0.", end="")
    else:
        if printShortDescription:
            print("Number of digits in a period of decinal expansion of " + str(number) + ": " + str(len(decimalExpansionList)))
            print("Decimal expansion of 1/" + str(number) + ": ", end="")
        print("0.", end="")
    for index, number in enumerate(decimalExpansionList):
        if index == periodIndex:
            print("(", end="")
        print(number, end="")
    if currentRemainder == 0:
        print(wholeDivisionProduct, end="")
    else:
        print(")", end="")
    print("")


if __name__ == "__main__":
    for i in range(2, 100):
        calculateDecimalExpansion(i, True)
    #Line of code below currently takes more than 400s to compute
    calculateDecimalExpansion(60017)