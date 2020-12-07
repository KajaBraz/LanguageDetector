from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import plot_confusion_matrix, confusion_matrix, accuracy_score, f1_score
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
import text_handling


def train_data(training_data: dict):
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

    return vectorizer, naive_classifier


def predict(validation_data: dict, trained_vectorizer, naive_classifier):
    # vectorizing validation data
    validation_labels, validation_sentences = [], []
    for language, sentences in validation_data.items():
        for sentence in sentences:
            validation_sentences.append(sentence)
            validation_labels.append(language)
    validation_vectors = trained_vectorizer.transform(validation_sentences)

    # predict
    predictions = naive_classifier.predict(validation_vectors)

    return validation_labels, validation_vectors, predictions


def show_stats(validation_labels, validation_vectors, predictions, naive_classifier):
    print('f1 score: ', f1_score(validation_labels, predictions, average='weighted'))
    plot_confusion_matrix(naive_classifier, validation_vectors, validation_labels, normalize='true')
    plt.show()
    plt.savefig('confusion_matrix.pdf')


def count_probabilities(predictions):
    occurrences = {}
    for language in predictions:
        if language in occurrences.keys():
            occurrences[language] += 1
        else:
            occurrences[language] = 1

    probabilities = {k: 100 * v / sum(list(occurrences.values())) for k, v in occurrences.items()}
    return probabilities


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

    vect, classifier = train_data(lang_data_dict)
    valid_labels, valid_vect, predicted = predict(validation_lang_data_dict, vect, classifier)
    show_stats(valid_labels, valid_vect, predicted, classifier)
    # print(count_probabilities(predicted))
