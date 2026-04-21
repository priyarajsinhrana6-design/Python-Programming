list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

list3 = list1 + list2
print(list3)

del list1[3]
print(list1)

list1.append("Java")
print(list1)

list2[3] = 11
print(list2)


del list2[2]
print(list2)


for i in range(4):
    print("Welcome to Marwadi University")

print(list1[-2])
print(list2[1:3])
print(list1[-1:-3])   # This will give empty list

print(len(list2))

print(max(list1))


print(min(list2))

list2.append(100)
print(list2)

list2.extend([200, 300])
print(list2)

list2 = [1, 2, 3, 4, 3]

# remove removes first matching value
list2.remove(3)
print(list2)

# pop removes by index
list2.pop(2)
print(list2)

list1.reverse()
print(list1)

list2.sort(reverse=True)
print(list2)

