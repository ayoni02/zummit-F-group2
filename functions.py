from transformers  import pipeline

def classify(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]

    result = classifier(text, labels)
    return result