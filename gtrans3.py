from texttranslator import deep3


def main():
    txt = 'Hello, how are you?'
    print('Original text:', txt)
    print('Language detection:', deep3.LangDetect(txt, 'all'))
    print('Translation to Ukrainian:', deep3.TransLate(txt, 'auto', 'uk'))
    print('Code for "uk":', deep3.CodeLang('uk'))


if __name__ == '__main__':
    main()
