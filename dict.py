vowels={'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
ask=input("Enter the string")
for w in ask:
    if w in vowels:
        vowels[w]+=1
print(vowels)