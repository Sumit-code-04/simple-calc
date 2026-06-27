# python simple calc using IF statement

operator = input("Enter an operator (+,-,*,/): ")
number1 = float(input("\nEnter the 1st Number: "))
numbar2 = float(input("Enter the 2nd Number: "))

if operator == "+":
  result = number1 + numbar2
  print(f"\nThe Addition is:{round(result,2)}")
elif operator == "-":
  result = number1 - numbar2
  print(f"\nThe Subtraction is:{round(result,2)}")
elif operator == "*":
  result = number1 * numbar2
  print(f"\nThe Multiplication is:{round(result,2)}")
elif operator == "/":
  result = number1 / numbar2
  print(f"\nThe Division is:{round(result,2)}")
else:
  print(f"\n===> {operator} is Invalid operator")