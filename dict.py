alphabet={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
ask=input("Enter some words")
count=0
for w in ask:
    if w in alphabet:
        count=count+1
        alphabet[w]+=1
print("This is how many letters repeat: "+str(alphabet))
words=len(ask.split())
print("This is how many words you have in your sentence: "+str(count))