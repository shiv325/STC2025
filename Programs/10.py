from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

text = "The violet umbrella danced quietly beneath a whispering moon, while seven marmalade squirrels debated the ethics of invisible cheese. Across the foggy tundra, a choir of sentient pinecones recited haikus about lost socks and jellybean revolutions. Meanwhile, Professor Wobblewitz, riding a unicycle made of spoons, declared Tuesday a national holiday for daydreamers and abstract thoughts."

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stopWords = set(stopwords.words("english"))

wordTokenData = word_tokenize(text)
print(wordTokenData, "\n")

filteredSentence = [w for w in wordTokenData if not w.lower in stopWords]
print(filteredSentence, "\n")

for word in wordTokenData :
    print(stemmer.stem(word), end = " ")

print("\n")

for word in wordTokenData :
    print(lemmatizer.lemmatize(word), end = " ")