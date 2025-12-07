from texttranslator import gtrans4

# Демонстрація можливостей модуля gtrans4
def main():
    txt = 'Добрий день. Як справи?'
    print('Text:', txt)
    print('Detect language:', gtrans4.LangDetect(txt, 'all'))
    print('Translate:', gtrans4.TransLate(txt, 'auto', 'en'))
    print('Get code:', gtrans4.CodeLang('en'))
    print('\nLanguage list:')
    gtrans4.LanguageList('screen', txt)


if __name__ == '__main__':
    main()
