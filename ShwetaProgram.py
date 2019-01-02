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


print("Hello, world!")

inputNumbers = [1, 2, 3, 4, 5, 15]

print("lol tough luck for you, no inputting your own numbers haha")
print("(Don't worry, that'll come later)")

algebraList = []
for number in inputNumbers:
    if number != inputNumbers[-1]:
        algebraList.append(number)
        algebraList.append("+")
    else:
        algebraList.pop()


print(algebraList)

evalString = ''.join(str(e) for e in algebraList)
evalResult = eval(evalString)
print("=" + str(evalResult))

if evalResult != inputNumbers[-1]:
    print("Math does not compute")
else:
    print("Math checks out")


#while(evalResult != inputNumbers[-1]):







