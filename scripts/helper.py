import collections
from tempfile import mkdtemp
from shutil import rmtree

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def get_all_words(list_names):
    list_names = cuts_off_special_names(list_names)
    list_words = []
    for name in list_names:
        list_words.append(name.split('_'))
    words = [x for x in flat(list_words) if x != '']
    return words


def cuts_off_special_names(list_items):
    list_names = []
    for name in list_items:
        if not (name.startswith('__') and name.endswith('__')):
            list_names.append(name)
    return list_names


def tuple_uniq_words(list_words, top_size=10):
    c = collections.Counter()
    for word in list_words:
        c[word] += 1
    tuple_words = c.most_common(top_size)
    return tuple_words


def mk_dir(repo_url='words_statistic'):
    dir_prefix = str(repo_url).split('/')[-1]
    repo_dir = mkdtemp(prefix='{}{}'.format(dir_prefix, '_'))
    return repo_dir


def rm_dir(folder):
    try:
        rmtree(folder)
    except OSError as e:
        logging.info('{}'.format(e))

