file = open("sample.txt","r")
data = file.read()
print(data)

words = data.split()
count = len(words)

print("Number of words:",count)

file.close()