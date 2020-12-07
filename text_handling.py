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
    for sentence in text:
        words = sentence.split(' ')
        n += len(words)
        m.update(words)
    stats['num of words'] = n
    stats['number_of_unique_words'] = len(m)
    return stats


def preprocess(text: [str]) -> [str]:
    preprocessed = []
    for sentence in text:
        sentence = sentence.strip().lower()
        sentence = re.sub(r'[^\sa-z]+', '', sentence)

        if len(sentence) != 0:
            preprocessed.append(sentence)
    return preprocessed


def get_unique_words(text: [str]) -> set:
    words = ' '.join(text).split(' ')
    all_words = set(words)
    if '' in all_words:
        all_words.remove('')
    return all_words


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
    print(lang_data['ita'])
    print(lang_data['en'])

    lang_data_dict = {}
    for data_lang, content in lang_data.items():
        lang_data_dict[data_lang] = preprocess(content)
    print(lang_data_dict['ita'])
    print(lang_data_dict['en'])

    unique_words = {}
    for data_lang, content in lang_data_dict.items():
        unique_words[data_lang] = get_unique_words(content)
    print(unique_words)
    print(len(unique_words['ita']))

    print('stats before')
    for l in lang_data.keys():
        print(statistics(lang_data[l]))
    print('********************')
    print('stats after')
    for l in lang_data.keys():
        print(statistics(lang_data_dict[l]))
