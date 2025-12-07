# Text Translation Project

Python package for text translation using googletrans and deep_translator.

## Setup

Install dependencies:
```
pip install -r requirements.txt
```

## Run Demo

```
python gtrans4.py
python gtrans3.py
python deeptr.py
python filetr.py
```

## Project Structure

`texttranslator/` — Translation modules:
- `gtrans4.py` — googletrans (async support)
- `deep3.py` — deep_translator (Python < 3.13)
- `deep_langdetect.py` — deep_translator + langdetect

Demo scripts show module usage with Ukrainian sample text and popular language translations (en, uk, fr, it, pt).

`filetr.py` reads text from file, translates using config settings (max_chars, max_words, max_sentences).

## Virtual Environment

Project uses `Didovets/` virtual environment. Activate on Windows:
```
.\Didovets\Scripts\Activate.ps1
```
