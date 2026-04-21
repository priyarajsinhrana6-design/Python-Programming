from functools import reduce

lst = [1,2,3,4,5]

square = list(map(lambda x: x*x, lst))
print(square)

even = list(filter(lambda x: x%2==0, lst))
print(even)

sum = reduce(lambda a,b: a+b, lst)
print(sum)