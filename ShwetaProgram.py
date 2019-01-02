def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)


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
    print(algebraList)
    evalString = ''.join(str(e) for e in algebraList)
    evalResult = eval(evalString)
    print("=" + str(evalResult))
    print("Should be " + str(target))

    if evalResult != target:
        print("Math does not compute")
    else:
        print("Math checks out")


print("Hello, world!")

inputNumbers = [1, 2, 3, 4, 5, 10]

print("lol tough luck for you, no inputting your own numbers haha")
print("(Don't worry, that'll come later)")

algebraList = []
for number in inputNumbers:
    if number != inputNumbers[-1]:
        algebraList.append(number)
        algebraList.append("+")
    else:
        algebraList.pop()

while checkMath(algebraList, inputNumbers[-1]) != inputNumbers[-1]:
    for i in range(0, algebraList.count("+")):
        if i == 0:
            i = i + 1
        else:
            i = i + 2

        algebraList[i] = iterateSign(algebraList[i])








