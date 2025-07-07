from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    subjectivity_score = blob.sentiment.subjectivity
    sentiment_score = blob.sentiment.polarity  # Range: [-1.0, 1.0]

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, sentiment_score, subjectivity_score

# Example usage
text_input = input("Enter Sentence => ")
sentiment, score, subjectivity = analyze_sentiment(text_input)

print(f"Sentiment => {sentiment}")
print(f"Sentiment Score => {score:.2f}")
print(f"Subjectivity Score => {subjectivity:.2f}")