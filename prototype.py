import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])


# The above is just to install the transformers package if it is not already installed
# In case of errors, comment it all out and use "pip install transformers" to install the package install


from transformers import pipeline


def classify(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    labels = ["TOXIC", "AGGRESSIVE", "HATE SPEECH", 'INSULTIVE', 'SPAM', 'NSFW', 'SEXUAL']

    result = classifier(text, labels)
    return result


if __name__ == "__main__":
    text = input("Enter the text to classify: ")
    result = classify(text) # we can change this so the variable name to maybe tag so it is not mixed up in future with the one in the classify function
    print(
        f'This content is {result}, please remove it and be careful going forward')  # print a statement instead of just tage
