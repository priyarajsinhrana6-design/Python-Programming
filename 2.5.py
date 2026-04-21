def outer_function(x):

    def inner_function(y):
        return y * y

    return inner_function(x)


print(outer_function(4))
