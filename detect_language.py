from naive_bayes_model import train_data, predict, show_stats, count_probabilities
from text_handling import preprocess, prepare_data
from language_data import languages_data


def detect_language(sentence, languages_data):
    cleared = preprocess([sentence])

    lang_data = prepare_data(languages_data)
    lang_data_dict = {}

    for data_lang, content in lang_data.items():
        lang_data_dict[data_lang] = preprocess(content)

    possible_languages = {}

    for lang in lang_data.keys():
        possible_languages[lang] = cleared

    vect, classifier = train_data(lang_data_dict)

    labels, vectors, predictions = predict(possible_languages, vect, classifier)
    success = count_probabilities(predictions)
    return success


if __name__ == '__main__':
    print(detect_language(
        'mettiamo alla prova il modello di language detector, vediamo se il programma se la cava bene, è una grande sfida',
        languages_data))
