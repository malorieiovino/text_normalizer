import streamlit as st
from spellchecker import SpellChecker
import contractions
import re

# Define a dictionary for slang and abbreviation translations
slang_dict = {
    "omg": "oh my god",
    "idk": "i do not know",
    "ik": "i know", 
    "wut": "what",
    "u": "you",
    "ur": "your",
    "brb": "be right back",
    "lol": "laughing out loud",
    "ttyl": "talk to you later",
    "btw": "by the way",
    "b4": "before",
    "gr8": "great",
    "thx": "thanks",
    "pls": "please",
    "cuz": "because", 
    "tysm": "thank you so much", 
    "lmao": "laughing my ass off", 
    "lmfao": "laughing my fucking ass off", 
    "ode": "overdoing it", 
    "ijbol": "I just burst out laughing", 
    "dtm": "doing too much", 
    "fr": "for real", 
    "srs": "serious", 
    "ty": "thank you", 
    "bc": "because", 
    "smh": "shaking my head", 
    "tbh": "to be honest", 
    "rn": "right now", 
    "rq": "right quick", 
    "nvm": "never mind", 
    "jk": "just kidding", 
    "np": "no problem", 
    "ppl": "people", 
    "fml": "fuck my life",
    "omfg": "oh my fucking god", 
    "wtf": "what the fuck", 
    "tho": "though", 
    "bro": "brother", 
    "hbu": "how about you", 
    "wbu": "what about you", 
    "ikr": "I know right", 
    "yw": "you're welcome", 
    "ikr": "I know right", 
    "idc": "I don't care", 
    "bday": "birthday", 
    "yk": "you know", 
    "w": "with", 
    "imo": "in my opinion", 
    "atm": "at the moment", 
    "sus": "suspicious", 
    "cap": "a lie", 
    "bet": "okay, agreed", 
    "dm": "direct message", 
    "dms": "direct messages", 
    "og": "original", 
    "tfw": "that feeling when", 
    "irl": "in real life", 
    "kinda": "kind of", 
    "sorta": "sort of", 
    "fire": "amazing", 
    "lit": "awesome"
    
    
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
