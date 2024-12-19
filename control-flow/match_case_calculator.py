num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=str(input("Choose the operation (+, -, *, /):"))
match operator:
    case '+':
        print(f"The result is {num1 + num2}")
    case '-':
        print(f"The result is {num1 - num2}")
    case '*':
        print(f"The result is {num1 * num2}")
    case '/':
        if num2 == 0:
            print("cannot divided by zero")
        else:
            print(f"The result is {num1 / num2}")
    case _:
        print("Invalid operator. Please choose from +, -, *, or /.")
