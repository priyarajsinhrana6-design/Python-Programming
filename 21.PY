try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print("Result:", c)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception:
    print("Some error occurred")