def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom float(denominator)
            if denom == 0:
                return "Error: Cannot divide by zero."
            return f"The result of the division is {num / denom}"
        except ValueError:
            return "Error: please enter numeric values only."
