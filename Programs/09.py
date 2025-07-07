import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

text = "The violet umbrella danced quietly beneath a whispering moon, while seven marmalade squirrels debated the ethics of invisible cheese. Across the foggy tundra, a choir of sentient pinecones recited haikus about lost socks and jellybean revolutions. Meanwhile, Professor Wobblewitz, riding a unicycle made of spoons, declared Tuesday a national holiday for daydreamers and abstract thoughts."

wordTokenData = word_tokenize(text)
print(wordTokenData, "\n")

sentTokenData = sent_tokenize(text)
print(sentTokenData, "\n")

stopWords = set(stopwords.words("english"))
filteredSentence = [w for w in wordTokenData if not w.lower in stopWords]
print(filteredSentence, "\n")
filteredSentence = []

for word in wordTokenData :
    if word not in stopWords :
        filteredSentence.append(word)
print(filteredSentence)