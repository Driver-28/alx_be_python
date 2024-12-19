num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
operator=str(input("Choose the operation (+, -, *, /):"))
if operator == '+':
    print(f"The result is {num1 + num2}")
elif operator == '-':
    print(f"The result is {num1 - num2}")
elif operator == '*':
    print(f"The result is {num1 * num2}")
elif operator == '/':
        if num2 == 0:
            print("cannot divided by zero")
        else:
            print(f"The result is {num1 / num2}")
