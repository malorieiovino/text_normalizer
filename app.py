import streamlit as st
import re
import contractions
from spellchecker import SpellChecker

# Set page configuration
st.set_page_config(
    page_title="Text Normalizer",
    page_icon="📝",
    layout="centered"
)

# Inject custom CSS
st.markdown(
    """
    <style>
    .title { text-align: center; font-size: 2.5em; font-weight: bold; }
    .stTextArea textarea { font-size: 16px; line-height: 1.5; }
    .stButton button { background-color: #4CAF50; color: white; border: none; padding: 10px 24px; border-radius: 4px; cursor: pointer; }
    .stButton button:hover { background-color: #45a049; }
    </style>
    """,
    unsafe_allow_html=True
)

# App header
st.image("https://raw.githubusercontent.com/malorieiovino/text_normalizer/main/phone.gif", width = 150)
st.markdown('<p class="title">Text Normalizer</p>', unsafe_allow_html=True)

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.write("Paste your text in the main area and click the button to normalize it.")

# Define a dictionary for slang and abbreviation translations
slang_dict = {
    "omg": "oh my god",
    "idk": "i do not know",
    "wut": "what",
    "u": "you",
    "ur": "your",
    "brb": "be right back",
    "r": "are", 
    "lol": "laughing out loud",
    "ttyl": "talk to you later",
    "btw": "by the way",
    "b4": "before",
    "gr8": "great",
    "thx": "thanks",
    "pls": "please",
    "plz": "please", 
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
    "lit": "awesome", 
    "ik": "I know", 
    "idek": "I don't even know", 
    "idec": "I don't even care", 
    "afaik": "as far as I know", 
    "rofl": "rolling on the floor laughing", 
    "rotfl": "rolling on the floor laughing", 
    "ily": "I love you", 
    "ilysm": "I love you so much",
    "asap": "as soon as possible", 
    "lmk": "let me know", 
    "tmi": "too much information", 
    "info": "information", 
    "sry": "sorry", 
    "icymi": "in case you missed it", 
    "fyi": "for your information", 
    "fomo": "fear of missing out", 
    "roi": "return on investment", 
    "bogo": "buy one get one", 
    "faq": "frequently asked questions", 
    "eta": "estimated time of arrival", 
    "tia": "thanks in advance", 
    "eod": "end of day", 
    "k": "okay", 
    "kk": "okay", 
    "ok": "okay", 
    "diy": "do it yourself", 
    "aka": "also known as", 
    "stfu": "shut the fuck up", 
    "tldr": "too long don't read", 
    "jw": "just wondering", 
    "jfc": "jesus fucking christ", 
    "omw": "on my way", 
    "ffs": "for fucks sake", 
    "ngl": "not gonna lie", 
    "iso": "in search of", 
    "hmu": "hit me up", 
    "wyd": "what are you doing", 
    "idgaf": "I don't give a fuck", 
    "tbd": "to be determined", 
    "tbf": "to be fair", 
    "tba": "to be announced", 
    "iykyk": "if you know you know", 
    "jic": "just in case", 
    "abt": "about", 
    "gtg": "got to go", 
    "pmo": "piss me off", 
    "pov": "point of view", 
    "hbd": "happy birthday", 
    "tw": "trigger warning", 
    "imho": "in my humble opinion", 
    "ooo": "out of office", 
    "ig": "i guess", 
    "rt": "retweet", 
    "tbt": "throwback", 
    "bf": "boyfriend", 
    "gf": "girlfriend", 
    "bff": "best friend", 
    "wcw": "woman crush wednesday", 
    "pda": "public display of affection", 
    "ltr": "long term relationship", 
    "loml": "love of my life", 
    "acct": "account", 
    "appt": "appointment", 
    "apt": "apartment", 
    "af": "as fuck", 
    "cmon": "come on", 
    "cu": "see you", 
    "dl": "down low", 
    "fwb": "friends with benefits", 
    "fwd": "forward", 
    "gl": "good luck", 
    "gm": "good morning", 
    "gn": "good night", 
    "hw": "homework", 
    "msg": "message", 
    "nm": "nothing much", 
    "nbd": "no big deal", 
    "dw": "don't worry", 
    "rly": "really", 
    "prob": "probably", 
    "prolly": "probably", 
    "ruok": "are you okay", 
    "y": "why", 
    "sec": "second", 
    "sup": "what's up", 
    "yktv": "you know the vibe" 
    
    
    
    
    
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
    
    # Translate slang and abbreviations
    words = [slang_dict[word] if word in slang_dict else word for word in words]
    
    # Correct spelling with a fallback to the original word
    spell = SpellChecker()
    corrected_words = []
    for word in words:
        # If the token contains spaces, assume it's a slang expansion and skip spell correction
        if " " in word:
            corrected_words.append(word)
        else:
            # Apply spell correction
            corrected = spell.correction(word)
            corrected_words.append(corrected if corrected else word)
    
    # Reassemble the cleaned text
    normalized_text = ' '.join(corrected_words)
    
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
