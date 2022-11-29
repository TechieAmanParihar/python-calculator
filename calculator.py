first = int(input("Enter Your First Number:"))
operator = input("Enter Operator (+,-,*,/,%):")
second = int(input("Enter Your Second Number:"))

first=int(first)
second=int(second)

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("Invalid")
    
    