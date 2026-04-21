lst = []

while True:
    print("1.Add")
    print("2.Delete")
    print("3.Display")
    print("4.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter number: "))
        lst.append(x)

    elif ch == 2:
        x = int(input("Enter number to remove: "))
        lst.remove(x)

    elif ch == 3:
        print(lst)

    elif ch == 4:
        break