from transformers  import pipeline
import streamlit as st


classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify(text):    
    labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    result = classifier(text, labels)
    return result

if __name__ == "__main__":
    text = st.text_input("Enter the text to classify: ") #input("Enter the text to classify: ")
    result = classify(text)
    st.write(result)