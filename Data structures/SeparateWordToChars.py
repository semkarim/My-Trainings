chars = []
word = input("Enter the word: ")

print(len(word))

for i in range (0,len(word)):
    chars.append(word[i])

print(chars)

for i in range (0,len(chars)):
    print(chars[i])