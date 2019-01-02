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
    #print(algebraList)
    evalString = ''.join(str(e) for e in algebraList)
    print(evalString)
    evalResult = eval(evalString)
    print("=" + str(evalResult))
    #print("Should be " + str(target))

    if int(evalResult) != int(target):
        #print("Math does not compute")
        return False
    else:
        #print("Math checks out")
        print(evalString + "=" + target)
        exit(0)

def cycleDown():
    



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

#for i in range(1, len(algebraList), 2):
#    for k in range(0, 4):
#        algebraList[i] = iterateSign(algebraList[i])
#        checkMath(algebraList, inputNumbers[-1])

cycleDown()

print("No match found :(")
