class safe_divide:
    def __init__(self, numerator, denominator):
        try:
            self.numerator = float(numerator)
            self.denominator = float(denominator)
            if self.denominator == 0:
                print("Error: Cannot divide by zero.")
                self.denominator = 1.0
        except ValueError:
            print("Error: Please enter numeric values only.")
            self.numerator = 0.0
            self.denominator = 1.0
    def safe_divide(self):
        try:
            result = self.numerator / self.denominator
            print(f"The result of the division is {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
