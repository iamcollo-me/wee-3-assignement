import spacy

# Load spaCy
nlp = spacy.load("en_core_web_sm")

# Simple reviews analysis
reviews = [
    "Great iPhone from Apple!",
    "Bad Samsung phone.",
    "Love my Sony headphones."
]

for review in reviews:
    doc = nlp(review)
    
    # Find entities
    entities = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT"]]
    
    # Simple sentiment based on keywords
    positive_words = ["great", "love", "good", "excellent", "amazing"]
    negative_words = ["bad", "terrible", "worst", "disappointed"]
    
    sentiment = "neutral"
    if any(word in review.lower() for word in positive_words):
        sentiment = "positive"
    elif any(word in review.lower() for word in negative_words):
        sentiment = "negative"
    
    print(f"Review: {review}")
    print(f"Entities: {entities}")
    print(f"Sentiment: {sentiment}\n")