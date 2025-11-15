from texttranslator import deep_langdetect


def demo():
    txt = 'Bonjour! Comment ça va?'
    print('Original:', txt)
    print('Detect:', deep_langdetect.LangDetect(txt, 'all'))
    print('Translate to en:', deep_langdetect.TransLate(txt, 'auto', 'en'))
    print('CodeLang fr ->', deep_langdetect.CodeLang('fr'))


if __name__ == '__main__':
    demo()
