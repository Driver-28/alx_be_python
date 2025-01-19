class safe_divide:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def divide(self):
        try:
            num = float(self.numerator)
            denom float(self.denominator)
            if denom == 0:
                return "Error: Cannot divide by zero."
            return num / denom
        except ValueError:
            return "Error: please enter numeric values only."
