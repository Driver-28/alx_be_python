class safe_divide:
    def __init__(self, numerator, denominator):
        try:
            self.numerator = float(numerator)
            self.denominator = float(denominator)
        except ValueError:
            print("Error: Please enter numeric values only.")
            self.numerator = 0.0
            self.denominator = 1.0
    def safe_divide(self):
        try:
            if self.denominator == 0:
                print("Error: Cannot divide by zero.")
                return None
            result = self.numerator / self.denominator
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None
