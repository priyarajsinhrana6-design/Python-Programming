import logging

logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    result = a / b
    print("Result:", result)
except ArithmeticError as e:
    logging.error("Arithmetic exception occurred")
    print("Arithmetic error occurred")