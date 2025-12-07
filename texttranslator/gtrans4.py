# Модуль для перекладу за допомогою googletrans
# автор: Didovets
# дата: 07.12.2025

from typing import Optional
try:
    from googletrans import Translator, LANGUAGES
except Exception:
    Translator = None
    LANGUAGES = {}


def _to_code(lang: str) -> Optional[str]:
    if not lang:
        return None
    v = lang.strip().lower()
    for code in LANGUAGES.keys():
        if v == code.lower():
            return code
    for code, name in LANGUAGES.items():
        if v == name.lower():
            return code
    return None


def TransLate(text: str, src: str, dest: str) -> str:
    if Translator is None:
        return "Error: googletrans not installed"
    try:
        trans = Translator()
        dest_code = _to_code(dest) or dest
        result = trans.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Error in TransLate: {e}"


def LangDetect(text: str, what: str = 'all') -> str:
    if Translator is None:
        return "Error: googletrans not installed"
    try:
        trans = Translator()
        res = trans.detect(text)
        if what == 'lang':
            return res.lang
        if what == 'confidence':
            return str(res.confidence)
        return f"{res.lang},{res.confidence}"
    except Exception as e:
        return f"Error in LangDetect: {e}"


def CodeLang(lang: str) -> str:
    if not lang:
        return "Невідомий код або мова"
    v = lang.strip().lower()
    for code, name in LANGUAGES.items():
        if v == code.lower():
            return name
    for code, name in LANGUAGES.items():
        if v == name.lower():
            return code
    return "Невідомий код або мова"


def LanguageList(out: str = 'screen', text: Optional[str] = None) -> str:
    if Translator is None:
        return "Error: googletrans not installed"
    try:
        trans = Translator()
        items = sorted(LANGUAGES.items())
        col1 = max(len('Code'), max((len(k) for k, _ in items), default=4))
        col2 = max(len('Language'), max((len(v) for _, v in items), default=8))
        if text:
            col3 = max(len('Translation'), 40)
        else:
            col3 = 0

        lines = []
        header = f"{ 'Code'.ljust(col1) }  { 'Language'.ljust(col2) }"
        if text:
            header += f"  { 'Translation'.ljust(col3) }"
        lines.append(header)
        lines.append('-' * len(header))

        for code, name in items:
            row = f"{code.ljust(col1)}  {name.ljust(col2)}"
            if text:
                try:
                    tr = trans.translate(text, dest=code).text
                except Exception:
                    tr = '<err>'
                row += f"  {tr.ljust(col3)}"
            lines.append(row)

        output = '\n'.join(lines)
        if out == 'screen':
            print(output)
        else:
            with open(out, 'w', encoding='utf-8') as f:
                f.write(output)
        return 'Ok'
    except Exception as e:
        return f"Error in LanguageList: {e}"
