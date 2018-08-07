from downloader import clone_repo_to_folder
from ast_maker import get_trees
from trees_parser import get_list_objects_name
from result import output_format_choice
import sys

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def main(url, name_objects, part_of_speech, output_format):
    path = clone_repo_to_folder(url)
    trees = get_trees(path)
    list_objects_name = get_list_objects_name(trees, name_objects)
    return output_format_choice(list_objects_name, output_format, url, part_of_speech)


def parse_argv():
    if len(sys.argv) < 5 or len(sys.argv) > 5:
        return error_argv()
    git_url, name_objects, part_of_speech, output_format = sys.argv[1:]
    return main(git_url, name_objects, part_of_speech, output_format)


def error_argv():
    logging.info('{}' .format("Wrong arguments"))
    logging.info('{}' .format("Four arguments are needed: url, ast_object, part of speech, output format"))


if __name__ == '__main__':
    parse_argv()
