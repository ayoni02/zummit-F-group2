import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])

#The above is just to install the transformers package if it is not already installed



from transformers  import pipeline

def classify(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]

    result = classifier(text, labels)
    return result

if __name__ == "__main__":
    text = input("Enter the text to classify: ")
    result = classify(text)
    print(result)