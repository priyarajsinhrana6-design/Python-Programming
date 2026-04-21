def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


User = int(input('''
1. ADDITION
2. SUBTRACTION
3. MULTIPLY
4. DIVISION
'''))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operation = {
    1: add,
    2: sub,
    3: mul,
    4: div
}

func = operation.get(User)

if func:
    print("Result:", func(a, b))
else:
    print("Unknown operation")
