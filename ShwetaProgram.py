def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)







print("Hello, world!")

inputNumbers = [1, 2, 3, 4, 5, 15]

print("lol tough luck for you, no inputting your own numbers haha")
print("(Don't worry, that'll come later)")

algebraList = []
for number in inputNumbers:
    if number != inputNumbers[-1]:
        algebraList.append(number)
        algebraList.append("+")
algebraList.pop()

print(algebraList)






