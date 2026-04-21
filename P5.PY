largest = None

for i in range(10):
    num = int(input("Enter number: "))
    
    if num % 2 != 0:
        if largest == None or num > largest:
            largest = num

print("Largest odd number:", largest)