# Text Normalizer

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-orange)](https://share.streamlit.io/<your-username>/<your-repo-name>/app.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/<your-username>/<your-repo-name>.svg?style=flat-square)](https://github.com/<your-username>/<your-repo-name>/stargazers)
[![Forks](https://img.shields.io/github/forks/<your-username>/<your-repo-name>.svg?style=flat-square)](https://github.com/<your-username>/<your-repo-name>/network)
[![Issues](https://img.shields.io/github/issues/<your-username>/<your-repo-name>.svg?style=flat-square)](https://github.com/<your-username>/<your-repo-name>/issues)

An interactive **text normalization tool** built with **Streamlit**. This project takes informal, unstructured text (like social media posts or SMS messages) and converts it into a more formal or standardized format. It handles:

- **Contraction Expansion** (e.g., "don't" → "do not")  
- **Slang & Abbreviation Translation** (e.g., "omg" → "oh my god")  
- **Spelling Correction**  
- **Basic Cleanup** (e.g., removing special characters)

## Demo

Click the badge above or use this link:  
**[Live Demo](https://textnormalizer-bqw8arw4htdoxudetu7ddz.streamlit.app/)**


---

## Features

- **Expand Contractions:** Automatically replaces contractions like `can't` with `cannot`.
- **Slang & Abbreviation Dictionary:** Converts common internet slang like `brb` → `be right back`.
- **Spelling Checker:** Uses [pyspellchecker](https://pypi.org/project/pyspellchecker/) to correct typographical errors.
- **Interactive Web App:** Powered by [Streamlit](https://streamlit.io/).

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
