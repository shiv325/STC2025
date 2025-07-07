text = input("Enter Text => ")
offensiveWords = {"stupid", "assassination", "kill"}
words = text.split()
for i in range(len(words)) :
    if words[i] in offensiveWords :
        words[i] = "*" * len(words[i])
text = " ".join(words)
print(f"Modified Text => {text}")