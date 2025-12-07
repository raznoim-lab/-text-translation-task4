# Модуль для перекладу deep_translator + langdetect
# Визначення мови через langdetect бібліотеку

from typing import Optional

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        from deep_translator import GoogleTranslator
        src_param = None if src.lower() == 'auto' else src
        tr = GoogleTranslator(source=src_param or 'auto', target=dest)
        return tr.translate(text)
    except Exception as e:
        return f"Error in TransLate (deep_langdetect): {e}"


def LangDetect(text: str, what: str = 'all') -> str:
    try:
        from langdetect import detect_langs
        res = detect_langs(text)
        if not res:
            return 'unknown'
        best = res[0]
        if what == 'lang':
            return best.lang
        if what == 'confidence':
            return str(best.prob)
        return f"{best.lang},{best.prob}"
    except Exception as e:
        return f"Error in LangDetect (deep_langdetect): {e}"


def CodeLang(lang: str) -> str:
    try:
        from deep_translator import constants
        langs = getattr(constants, 'LANGUAGES', {})
        v = lang.strip().lower()
        for code, name in langs.items():
            if v == code.lower():
                return name
        for code, name in langs.items():
            if v == name.lower():
                return code
        return 'Невідомий код або мова'
    except Exception as e:
        return f"Error in CodeLang (deep_langdetect): {e}"


def LanguageList(out: str = 'screen', text: Optional[str] = None) -> str:
    try:
        from deep_translator import constants, GoogleTranslator
        langs = getattr(constants, 'LANGUAGES', {})
        lines = [f"Code  Language"]
        for code, name in sorted(langs.items()):
            if text:
                try:
                    tr = GoogleTranslator(source='auto', target=code).translate(text)
                except Exception:
                    tr = '<err>'
                lines.append(f"{code}  {name}  {tr}")
            else:
                lines.append(f"{code}  {name}")
        output = '\n'.join(lines)
        if out == 'screen':
            print(output)
        else:
            with open(out, 'w', encoding='utf-8') as f:
                f.write(output)
        return 'Ok'
    except Exception as e:
        return f"Error in LanguageList (deep_langdetect): {e}"
