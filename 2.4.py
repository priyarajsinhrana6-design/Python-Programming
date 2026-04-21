def simple_interest(principal, time, rate=5):
    return (principal * rate * time) / 100


print(simple_interest(1000, 2))        # default rate = 5
print(simple_interest(1000, 2, 10))    # custom rate
