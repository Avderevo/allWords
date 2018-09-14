from nltk import pos_tag

NLTK_TEGS = {'verb': ['VB', 'VBR'], 'noun': ['NNS', 'NN']}


def get_part_of_speech(word_list, part_of_speech):
    if str(part_of_speech).lower() in NLTK_TEGS.keys():
        list_part_of_speech = []
        for word in word_list:
            word = pos_tag([word])
            if word[0][1] in NLTK_TEGS[part_of_speech]:
                list_part_of_speech.append(word[0][0])
    return list_part_of_speech
