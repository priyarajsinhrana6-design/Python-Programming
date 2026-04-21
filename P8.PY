s = input("Enter string: ")

vowels = "aeiouAEIOU"
count = 0

for i in s:
    if i in vowels:
        count += 1

print("Vowel count:", count)

length = 0
for i in s:
    length += 1

print("Length:", length)

rev = s[::-1]
print("Reverse:", rev)

old = input("Enter word to replace: ")
new = input("Enter new word: ")
print(s.replace(old,new))

if s == rev:
    print("Palindrome")
else:
    print("Not palindrome")