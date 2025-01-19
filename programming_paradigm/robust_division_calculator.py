class safe_divide:
    def __init__(self, a, b):
        self.numerator = float(numerator)
        self.denominator = float(denominator)
    def safe_divide(self):
        try:
            result = self.numerator / self.denominator
            print(f"The result of the division is {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.")
