from transformers  import pipeline
import streamlit as st


classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify(text):    
    labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    run_pipe = classifier(text, labels)
    return run_pipe

def main():
    text = st.text_input("Enter the text to classify: ") #input("Enter the text to classify: ")
    results = classify(text)
    st.write(results)
    
main()