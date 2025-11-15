from googletrans import Translator, LANGUAGES


def _normalize_to_code(lang: str) -> str | None:
    """Return ISO code for a language name or code, or None if unknown."""
    if not lang:
        return None
    lang_lower = lang.strip().lower()
    # direct code match
    for code in LANGUAGES.keys():
        if lang_lower == code.lower():
            return code
    # name match
    for code, name in LANGUAGES.items():
        if lang_lower == name.lower():
            return code
    return None


def TransLate(text: str, lang: str) -> str:
    """Translate `text` into language `lang` (name or ISO code).

    Returns translated string or an error message.
    """
    try:
        code = _normalize_to_code(lang)
        if not code:
            return f"Помилка: невідома мова '{lang}'"
        translator = Translator()
        res = translator.translate(text, dest=code)
        return res.text
    except Exception as e:
        return f"Сталася помилка при перекладі: {e}"


def LangDetect(txt: str) -> str:
    """Detect language of `txt` and return a summary string with confidence."""
    try:
        translator = Translator()
        res = translator.detect(txt)
        return f"Detected(lang={res.lang}, confidence={res.confidence})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"


def CodeLang(lang: str) -> str:
    """If `lang` is a language name -> return its ISO code.
    If `lang` is a code -> return the language name.
    Otherwise return an informative string.
    """
    if not lang:
        return "Невідомий код або мова"
    lang_lower = lang.strip().lower()
    # code -> name
    for code, name in LANGUAGES.items():
        if lang_lower == code.lower():
            return name
    # name -> code
    for code, name in LANGUAGES.items():
        if lang_lower == name.lower():
            return code
    return "Невідомий код або мова"


if __name__ == '__main__':
    # Simple demo usage: try interactive input, otherwise use defaults
    try:
        txt = input('Enter text to translate (or leave empty for demo): ').strip()
    except Exception:
        txt = ''

    if not txt:
        txt = 'Доброго дня. Як справи?'

    try:
        lang = input('Enter target language (name or code, e.g. en or English): ').strip()
    except Exception:
        lang = ''

    if not lang:
        lang = 'en'

    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang(lang))
