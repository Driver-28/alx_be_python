class calculator:
    def __init__(self, numerator, denominator):
        self.numerator = numerator * 1.0
        self.denominator = denominator * 1.0 if denominator != 0 else 1
    def safe_divide(self, numerator, denominator):
        try:
            result = self.numerator / self.denominator
            print(f"The result of the division is {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.")
