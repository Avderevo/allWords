import json
import os
from downloader import create_folder
from word_anlitics import get_part_of_speech

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def output_format_choice(list_objects_name, output_format, url, part_of_speech):
    result_object_name = get_part_of_speech(list_objects_name, part_of_speech)
    if str(output_format) == 'json':
        return output_json(result_object_name, url)
    elif str(output_format) == 'csv':
        return output_csv(result_object_name, url)
    else:
        return output_console(result_object_name)


def output_json(result_objects, url):
    result_file = create_result_filename(url)
    dict_result = {i[0]: i[1] for i in result_objects}
    with open(result_file, 'w') as file:
        json.dump(dict_result, file)


def output_csv(result_objects, url):
    result_file = create_result_filename(url)
    with open(result_file, 'w') as file:
        for i in result_objects:
            file.write('{}: {}, ' .format(i[0], i[1]))


def output_console(result_objects):
    for i in result_objects:
        logging.info('{}: {}, ' .format(i[0], i[1]))


def create_result_filename(url):
    result_folder = create_folder(url, folder='result')
    result_file = os.path.join(result_folder, 'result_word_statistic')
    return result_file
