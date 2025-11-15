from texttranslator import deep3


def demo():
    txt = 'Hello, how are you?'
    print('Original:', txt)
    print('Detect:', deep3.LangDetect(txt, 'all'))
    print('Translate to uk:', deep3.TransLate(txt, 'auto', 'uk'))
    print('CodeLang uk ->', deep3.CodeLang('uk'))
    print('\nLanguage list preview:')
    print(deep3.LanguageList('screen', txt))


if __name__ == '__main__':
    demo()
