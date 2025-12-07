from texttranslator import gtrans4
import sys
import io

# Ensure UTF-8 output in Windows consoles (helps avoid mojibake)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except Exception:
        pass


def main():
    txt = 'Добрий день. Як справи?'
    print('Text:', txt)

    # If googletrans is not available, avoid calling translation functions
    if getattr(gtrans4, 'Translator', None) is None:
        print('googletrans not available. To enable translation, install dependencies:')
        print('  pip install -r requirements.txt')
        # CodeLang does not require googletrans to run (it uses LANGUAGES mapping),
        # so show it as an example.
        print('Get code:', gtrans4.CodeLang('en'))
        return

    # Normal demo flow
    try:
        print('Detect language:', gtrans4.LangDetect(txt, 'all'))
        print('Translate:', gtrans4.TransLate(txt, 'auto', 'en'))
        print('Get code:', gtrans4.CodeLang('en'))
        print('\nLanguage list (trimmed to 20):')
        # Trim the language list for readability in demo
        gtrans4.LanguageList('screen', txt, max_items=20)
    except Exception as e:
        print('Error while running demo:', e)


if __name__ == '__main__':
    main()
