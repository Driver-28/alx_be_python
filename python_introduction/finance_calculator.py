num1 = float(input("Enter your monthly income:"))
num2 = float(input("Enter your total monthly expenses:"))
Monthly_Savings = num1 - num2
projected_savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Your monthly savings are $",Monthly_savings.)
print("project savings after one year, with interest, is: $",projected_savings.)
