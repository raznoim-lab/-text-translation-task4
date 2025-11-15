from texttranslator import gtrans4


def demo():
    txt = 'Доброго дня. Як справи?'
    print('Original:', txt)
    print('Detect:', gtrans4.LangDetect(txt, 'all'))
    print('Translate to en:', gtrans4.TransLate(txt, 'auto', 'en'))
    print('CodeLang en ->', gtrans4.CodeLang('en'))
    print('\nLanguage list preview (first 10):')
    # print language list to screen (may be big)
    gtrans4.LanguageList('screen', txt)


if __name__ == '__main__':
    demo()
