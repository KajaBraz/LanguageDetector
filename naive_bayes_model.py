from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import plot_confusion_matrix, confusion_matrix, accuracy_score, f1_score
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import text_handling


def naive_bayes_model(training_data: dict, validation_data: dict):
    # vectorizing training data
    training_labels, training_sentences = [], []
    for language, sentences in training_data.items():
        for sentence in sentences:
            training_sentences.append(sentence)
            training_labels.append(language)

    vectorizer = CountVectorizer()
    training_vectors = vectorizer.fit_transform(training_sentences)

    # initializing model parameters and training
    naive_classifier = MultinomialNB()
    naive_classifier.fit(training_vectors, training_labels)

    # vectorizing validation data
    validation_labels, validation_sentences = [], []
    for language, sentences in validation_data.items():
        for sentence in sentences:
            validation_sentences.append(sentence)
            validation_labels.append(language)
    validation_vectors = vectorizer.transform(validation_sentences)

    # predict
    predictions = naive_classifier.predict(validation_vectors)

    # todo fix visualisation of the results

    res = confusion_matrix(validation_sentences, predictions)
    # print('Resutls')
    # print(res)
    # print('Accuracy score: ', accuracy_score(validation_sentences,predictions))
    print('f1 score: ', f1_score(validation_labels, predictions, average='weighted'))
    # plt.figure()
    # conf_mx = confusion_matrix(validation_labels, predictions, ['ita', 'en', 'pt'])
    fig = plt.figure()
    plt.plot(res)
    plt.show()

    return predictions


if __name__ == '__main__':
    languages_data = [('ita', 'italian_data.txt'), ('en', 'english_data.txt'), ('pt', 'portuguese_data.txt')]
    lang_data = text_handling.prepare_data(languages_data)
    lang_data_dict = {}

    validation_languages_data = [('ita', 'italian_validation_data.txt'), ('en', 'english_validation_data.txt'),
                                 ('pt', 'portuguese_validation_data.txt')]
    validation_lang_data = text_handling.prepare_data(validation_languages_data)
    validation_lang_data_dict = {}

    for data_lang, content in lang_data.items():
        lang_data_dict[data_lang] = text_handling.preprocess(content)
    # print(lang_data_dict)

    for validation_data_lang, validation_content in validation_lang_data.items():
        validation_lang_data_dict[validation_data_lang] = text_handling.preprocess(validation_content)
    # print(validation_lang_data_dict)

    naive_bayes_model(lang_data_dict, validation_lang_data_dict)
