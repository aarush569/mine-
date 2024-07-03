def calculate(a, op, b):
    if op == "*":
        return a * b
    elif op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b


a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))
op = input("enter the operator:")
print("the calculated value is:", calculate(a, op, b))