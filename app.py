from transformers  import pipeline
import streamlit as st


#classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")



def main():
    text = st.text_input("Enter the text to classify: ") #input("Enter the text to classify: ")
    if text:
        #results = classify(text)
        st.write()
    else:
        st.write("Please enter some text to classify")
    
main()