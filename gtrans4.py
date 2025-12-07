from texttranslator import gtrans4


def main():
    txt = 'Добрий день. Як справи?'
    print('Original text:', txt)
    print('Language detection:', gtrans4.LangDetect(txt, 'all'))
    print('Translation to English:', gtrans4.TransLate(txt, 'auto', 'en'))
    print('Code for "en":', gtrans4.CodeLang('en'))
    print('\nLanguage list with translation:')
    gtrans4.LanguageList('screen', txt)


if __name__ == '__main__':
    main()
