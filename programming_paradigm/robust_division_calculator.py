class calculator:
    def safe_divide(self, numerator, denominator):
        try:
            self.numerator = float (numerator)
            self.denominator = float (denominator)
            result = numerator / denominator
            print(f"The result of the division is {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except ValueError:
            print("Error: Please enter numeric values only.")
