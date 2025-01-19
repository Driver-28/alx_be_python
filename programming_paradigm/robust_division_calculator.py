class calculator:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator if denominator != 0 else 1
    def safe_divide(self, numerator, denominator):
        try:
            result = numerator / denominator
            print(f"The result of the division is {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.")
