from texttranslator import deep_langdetect


def main():
    txt = 'Bonjour! Comment ça va?'
    print('Original text:', txt)
    print('Language detection:', deep_langdetect.LangDetect(txt, 'all'))
    print('Translation to English:', deep_langdetect.TransLate(txt, 'auto', 'en'))
    print('Code for "fr":', deep_langdetect.CodeLang('fr'))


if __name__ == '__main__':
    main()
