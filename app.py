import streamlit as st
from spellchecker import SpellChecker
import contractions
import re

# Define a dictionary for slang and abbreviation translations
slang_dict = {
    "omg": "oh my god",
    "idk": "i do not know",
    "wut": "what",
    "u": "you",
    "brb": "be right back",
    "lol": "laughing out loud",
    "ttyl": "talk to you later",
    "btw": "by the way",
    "b4": "before",
    "gr8": "great",
    "thx": "thanks",
    "pls": "please",
    "cuz": "because"
}

def normalize_text(text: str) -> str:
    # Convert to lowercase
    text = text.lower()
    
    # Expand contractions
    text = contractions.fix(text)
    
    # Remove special characters but keep spaces
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Tokenize the text for processing
    words = text.split()
    
    # Translate slang and correct abbreviations
    words = [slang_dict[word] if word in slang_dict else word for word in words]
    
    # Correct spelling with a fallback to the original word
    spell = SpellChecker()
    words = [spell.correction(word) if spell.correction(word) else word for word in words]
    
    # Reassemble the cleaned text
    normalized_text = ' '.join(words)
    
    return normalized_text

# Streamlit UI
st.title("Text Normalization Tool")
st.write("This tool converts informal or unstructured text into a more formal, normalized format.")

# User input
user_input = st.text_area("Enter the text you want to normalize:")

if st.button("Normalize Text"):
    if user_input:
        normalized_text = normalize_text(user_input)
        st.write("### Normalized Text:")
        st.write(normalized_text)
    else:
        st.write("Please enter some text to normalize.")
