import re
import random


def read_text(text: str) -> list:
    with open(text, encoding="utf8") as f:
        return f.readlines()


def statistics(text: list) -> dict:
    stats = {'num of rows': len(text), 'num of words': 0, 'number_of_unique_words': 0,
             'sample_extract': random.choice(text)}
    n = 0
    m = set()
    # print(text)
    for sentence in text:
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(sentence)
        words = sentence.split(' ')
        n += len(words)
        m.update(words)
    stats['num of words'] = n
    stats['number_of_unique_words'] = len(m)
    return stats


def preprocess(text: list) -> list:
    """Takes a list of strings. Removes from the text punctuation, numbers, and other special signs. Returns plain
    text"""
    l = []
    for sentence in text:
        sentence = sentence.replace('/n', '').lower()
        preprocessed = ''
        for ch in sentence:
            if ch.isalpha():
                preprocessed += ch
            else:
                preprocessed += ' '
        l.append(preprocessed)

    ll = []
    for preprocessed in l:
        preprocessed = re.sub(' +', ' ', preprocessed)
        ll.append(preprocessed)

    lll = []
    for preprocessed in ll:
        if preprocessed[0] == ' ':
            preprocessed = preprocessed[1:]
        if preprocessed and preprocessed[-1] == ' ':
            preprocessed = preprocessed[:-1]
        lll.append(preprocessed)

    return lll


def get_unique_words(text: str) -> set:
    words = ' '.join(text).split(' ')
    return set(words)


def prepare_data(data: list) -> dict:
    """Takes a list of tuples and creates a dictionary with their first elements as keys; second elements,
    lists of strings, become the dict's values """
    d = {}
    for t in data:
        d[t[0]] = read_text(t[1])
    return d


if __name__ == '__main__':
    languages_data = [('ita', 'italian_data.txt'), ('en', 'english_data.txt'), ('pt', 'portuguese_data.txt')]
    lang_data = prepare_data(languages_data)
    # print(lang_data['ita'])
    # print(statistics(lang_data['ita']))

    lang_data_dict = {}
    for data_lang, content in lang_data.items():
        lang_data_dict[data_lang] = preprocess(content)
    print(lang_data_dict)

    # unique_words = {}
    # for data_lang, content in lang_data_dict.items():
    #     unique_words[data_lang] = get_unique_words(content)
    # print(unique_words)
    # print(len(unique_words['ita']))
    #
    print('stats before')
    for l in lang_data.keys():
        print(statistics(lang_data[l]))
    print('********************')
    print('stats after')
    for l in lang_data.keys():
        print(statistics(lang_data_dict[l]))
