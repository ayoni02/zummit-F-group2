from transformers  import pipeline
import streamlit as st
#from functions import classify

st.write("welcome")
#classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
#res = classify("i am a good boy")
#st.write(res)

@st.cache_data
def rata(txt):
    # Fetch data from URL here, and then clean it up.
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    return classifier

def main():
    text = st.text_input("Enter the text to classify: ") #input("Enter the text to classify: ")
    #labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    if text:
        results = rata(text)
        st.write(results['sequence'])
        st.write(results['labels'])
        st.write(results['scores'])
    else:
        st.write("Please enter some text to classify")
    
main()