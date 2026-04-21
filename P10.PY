add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b

a = int(input("Enter number: "))
b = int(input("Enter number: "))
op = input("Enter operator: ")

if op == "+":
    print(add(a,b))
elif op == "-":
    print(sub(a,b))
elif op == "*":
    print(mul(a,b))
elif op == "/":
    print(div(a,b))