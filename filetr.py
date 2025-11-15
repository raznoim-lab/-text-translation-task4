import json
import os
from texttranslator import gtrans4, deep_langdetect, deep3


def read_config(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def analyze_file(path: str) -> dict:
    if not os.path.exists(path):
        return {'error': 'file not found'}
    text = open(path, 'r', encoding='utf-8').read()
    size = os.path.getsize(path)
    chars = len(text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    # attempt detect
    det = gtrans4.LangDetect(text, 'all')
    return {
        'filename': os.path.basename(path),
        'size': size,
        'chars': chars,
        'words': words,
        'sentences': sentences,
        'lang': det,
        'text': text,
    }


def run_from_config(cfg_path: str):
    cfg = read_config(cfg_path)
    infile = cfg.get('input_file')
    out_mode = cfg.get('out', 'screen')
    module = cfg.get('module', 'gtrans4')
    lang = cfg.get('lang', 'en')
    max_chars = cfg.get('max_chars')
    max_words = cfg.get('max_words')
    max_sentences = cfg.get('max_sentences')

    info = analyze_file(infile)
    if 'error' in info:
        print(info['error'])
        return

    print('File:', info['filename'])
    print('Size:', info['size'])
    print('Chars:', info['chars'])
    print('Words:', info['words'])
    print('Sentences:', info['sentences'])
    print('Detected:', info['lang'])

    # read piecewise
    text = info['text']
    chosen = ''
    cur_chars = cur_words = cur_sentences = 0
    parts = text.split('\n')
    for line in parts:
        if max_chars and cur_chars >= max_chars:
            break
        if max_words and cur_words >= max_words:
            break
        if max_sentences and cur_sentences >= max_sentences:
            break
        chosen += line + '\n'
        cur_chars += len(line)
        cur_words += len(line.split())
        cur_sentences += line.count('.') + line.count('?') + line.count('!')

    # choose module
    translator = None
    if module == 'gtrans4':
        translator = gtrans4
    elif module == 'deep3':
        translator = deep3
    elif module == 'deep_langdetect':
        translator = deep_langdetect
    else:
        print('Unknown module in config')
        return

    # perform translation
    result = translator.TransLate(chosen, 'auto', lang)

    if out_mode == 'screen':
        print('---- Translation (', lang, ') ----')
        print(result)
    else:
        outname = infile + f'.{lang}.translated.txt'
        with open(outname, 'w', encoding='utf-8') as f:
            f.write(result)
        print('Ok')


if __name__ == '__main__':
    cfg = 'filetr_config.json'
    if os.path.exists(cfg):
        run_from_config(cfg)
    else:
        print('Config file filetr_config.json not found.')
