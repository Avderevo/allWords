import json
from helper import tuple_uniq_words, mk_dir
import os
import csv

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def output_format_choice(result_list, top_size, out_format, part_of_speech):
    file_name = make_name(out_format, part_of_speech)
    result_tuple = tuple_uniq_words(result_list, top_size)

    if str(out_format).lower() == 'json':
        return output_json(result_tuple, file_name)
    elif str(out_format).lower() == 'csv':
        return output_csv(result_tuple, file_name)
    else:
        logging.info('Invalid output format!')
        return


def output_json(result_tuple, file_name):

    result = {i[0]: i[1] for i in result_tuple}
    dir_name = mk_dir()
    with open(os.path.join(dir_name, file_name), 'w') as file:
        json.dump(result, file)
    logging.info(
        '\n\033[33mThe result file is saved to the directory "{}"'.format(dir_name))


def output_csv(result_tuple, file_name):
    dir_name = mk_dir()
    with open(os.path.join(dir_name, file_name), 'w') as file:
        writer = csv.writer(file)
        for row in result_tuple:
            writer.writerow(row)        
    logging.info(
        '\n\033[33mThe result file is saved to the directory "{}"'.format(dir_name))
    

def output_console(result, top_size, part_of_speech):

    result = tuple_uniq_words(result, top_size)
    real_top = len(result)
    part = 'verbs'

    if str(part_of_speech).lower() == 'noun':
        part = 'nouns'

    top_word = '  Top {} {}:'.format(real_top, part)

    R = '\n\033[33m{:>12}\x1b[0m\n'.format(top_word)

    for i in result:

        R += '\033[33m  {0:10} --- {1:1}\x1b[0m\n'.format(i[0], i[1])
    logging.info(R)


def make_name(out_format, part_of_speech):
    file_name = 'top_{}.{}'.format(part_of_speech, out_format)
    return file_name


