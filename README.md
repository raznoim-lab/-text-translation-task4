# Text Translation Project

A Python package for text translation using multiple translation services.

## Structure

- `texttranslator/` — Package with three translation modules:
  - `gtrans4.py` — Using googletrans 4.0.2
  - `deep3.py` — Using deep_translator 3.1.0a0 (Python < 3.13)
  - `deep_langdetect.py` — Using deep_translator with langdetect
- `gtrans4.py` — Demonstration script for gtrans4 module
- `gtrans3.py` — Demonstration script for deep3 module (requires Python 3.12 or lower)
- `deeptr.py` — Demonstration script for deep_langdetect module
- `filetr.py` — Text file translation program with configuration file
- `input_text.txt` — Sample text file for translation
- `filetr_config.json` — Configuration file for filetr.py

## How to Run

1. Activate virtual environment:
   ```
   .\Didovets\Scripts\Activate.ps1
   ```

2. Run demonstration scripts:
   ```
   python gtrans4.py
   python deeptr.py
   python filetr.py
   ```

## Requirements

See `requirements.txt` for all dependencies.
