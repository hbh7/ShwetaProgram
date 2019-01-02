def iterateSign(sign):
    if sign == "+":
        sign = "-"
    elif sign == "-":
        sign = "*"
    elif sign == "*":
        sign = "/"
    elif sign == "/":
        sign = "+"
    return sign

def checkMath(algebraList, target):
    evalString = ''.join(str(e) for e in algebraList)
    evalResult = eval(evalString)

    if int(evalResult) != int(target):
        return False
    else:
        print(evalString + "=" + target)
        exit(0)

def cycleDown(algebraList, i):
    if i < len(algebraList):
        checkMath(algebraList, inputNumbers[-1])
        for k in range(0, 4):
            algebraList[i] = iterateSign(algebraList[i])
            checkMath(algebraList, inputNumbers[-1])
            cycleDown(algebraList, i+2)


inputString = input("Please enter a string of numbers separated by spaces and ending in the total sum: ")
inputNumbers = inputString.split(" ")

algebraList = []
for number in inputNumbers:
    algebraList.append(number)
    algebraList.append("+")
algebraList.pop()
algebraList.pop()
algebraList.pop()

checkMath(algebraList, inputNumbers[-1])

cycleDown(algebraList, 1)

print("No match found :(")
