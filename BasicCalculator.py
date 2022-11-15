def add(x, y):
    answer = x + y
    print(str(x) + " + " + str(y) + " = " + str(answer))


def sub(x, y):
    answer = x - y
    print(str(x) + " - " + str(y) + " = " + str(answer))


def mul(x, y):
    answer = x * y
    print(str(x) + " * " + str(y) + " = " + str(answer))


def div(x, y):
    answer = x / y
    print(str(x) + " / " + str(y) + " = " + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")


    choice = input("Input your choice: ")


    if choice == "a" or choice =="A":
        print("Addition")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        add(x, y)
    if choice == "b" or choice =="B":
        print("Subtraction")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        sub(x, y)
    if choice == "c" or choice =="C":
        print("Multiplication")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        mul(x, y)
    if choice == "d" or choice == "D":
        print("Division")
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        div(x, y)
    if choice == "e" or choice == "E":
        print("Program ended.")
        break