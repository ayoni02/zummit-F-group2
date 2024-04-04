from transformers import pipeline
import streamlit as st

# from functions import classify

st.write("Comment Moderation Model for Toxicity DetectionTask")
st.write("""
        Description:
        In response to the growing concern over the proliferation of toxic comments within online communities, within the context of the Zummit Community Learning platform, we aim to develop a sophisticated model capable of effectively identifying and flagging toxic comments. The proliferation of toxic comments, characterized by harmful language, offensive content, and disruptive behavior, presents a significant challenge to fostering a positive and inclusive online environment.
        As such, this project seeks to leverage cutting-edge machine learning techniques and natural language processing (NLP) algorithms to analyze user-generated content and automatically detect instances of toxicity.
        The primary objective of this initiative is to enhance community engagement and promote constructive discourse by proactively identifying and addressing toxic behavior within the Zummit platform. Build an advanced comment moderation model, that will mitigate the adverse effects of toxic comments and uphold the community's standards of respect, civility, and inclusivity.
        """)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")


def main():
    text = st.text_input("Enter the text to classify: ")  # input("Enter the text to classify: ")
    labels = ["TOXIC", "AGGRESSIVE", "HATE SPEECH", "INSULTIVE", "SPAM", "NSFW", "SEXUAL HARASSMENT", "NEUTRAL", "POSITIVE"]
    if text:
        results = classifier(text, labels)
        # st.write(results['sequence'])
        st.write(results['labels'][0])
        st.write(int(results['scores'][0])*100)
        if results['labels'][0] != ("NEUTRAL" or "POSITIVE"):
            st.write(f"This post is considered {results['labels'][0]}, please review you words.")
    else:
        st.write("Please enter some text to classify")
    st.write("")


main()
