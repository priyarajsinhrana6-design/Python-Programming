def calculate(a,b,op):

    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b

a = int(input("Enter number: "))
b = int(input("Enter number: "))
op = input("Enter operator: ")

print(calculate(a,b,op))