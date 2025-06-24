from transformers import pipeline

# Load model once at startup
sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text: str):
    return sentiment_pipeline(text)[0]
