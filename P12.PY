x = 10

def outer():
    y = 20

    def inner():
        nonlocal y
        global x
        y = y + 5
        x = x + 5
        print("Inner y:",y)

    inner()
    print("Outer y:",y)

outer()
print("Global x:",x)