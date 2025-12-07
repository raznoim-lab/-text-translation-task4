from texttranslator import gtrans4
import sys
import io

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

    if getattr(gtrans4, 'Translator', None) is None:
        print('googletrans not installed. pip install -r requirements.txt')
        print('Get code:', gtrans4.CodeLang('en'))
        return

    try:
        print('Detect language:', gtrans4.LangDetect(txt, 'all'))
        print('Translate:', gtrans4.TransLate(txt, 'auto', 'en'))
        print('Get code:', gtrans4.CodeLang('en'))
        print('\nPopular languages:')
        popular = ['en', 'ru', 'uk', 'de', 'fr', 'es', 'it', 'pl', 'pt', 'nl']
        gtrans4.LanguageList('screen', txt, langs=popular)
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    main()
