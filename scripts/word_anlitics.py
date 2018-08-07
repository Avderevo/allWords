from nltk import pos_tag
import nltk
from helper import dict_uniq_words

nltk.download('averaged_perceptron_tagger')


NLTK_TEGS = {'verb': ['VB', 'VBR'], 'noun': ['NNS', 'NN']}


def get_part_of_speech(list_words, part_of_speech):
    if str(part_of_speech) in NLTK_TEGS.keys():
        list_part_of_speech = []
        for word in list_words:
            word = pos_tag([word])
            if word[0][1] in NLTK_TEGS[part_of_speech]:
                list_part_of_speech.append(word[0][0])
    return dict_uniq_words(list_part_of_speech)
