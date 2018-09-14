import argparse
from downloader import clone_repo
from ast_maker import get_trees
from trees_parser import get_list_objects_name
from result import output_format_choice, output_console
from partspeech import get_part_of_speech
from helper import mk_dir, rm_dir

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--dirs',
        dest='dir_path',
        help='The path to the project.'
    )
    parser.add_argument(
        '-t', '--top',
        default=10,
        dest='top_size',
        type=int,
        help='The size of the top verbs, default is 10.',
    )
    parser.add_argument(
        '--repo',
        help='URL of the project repository.',
        dest='repo_url',
    )
    parser.add_argument(
        '-c', '--category',
        help='Select a "noun" if you want statistics of nouns.'
        'Or "verb" if statistics verbs. "verb" are by default.',
        default='verb',
        dest='word_category',
        choices=['noun', 'verb']
    )
    parser.add_argument(
        '-n', '--name',
        help='Choose: "verb" - if you keep verbs.'
             '"noun" - if you want nouns.'
             '"class" - if you want statistics on classe names',
        default='func',
        dest='names',
        choices=['var', 'func', 'class']
    )
    parser.add_argument(
        '-o', '--output',
        dest='output',
        help='Report output method.'
        'Possible value: console - output result script to console, '
             'file - output result script to file.',
        default='console',
        choices=['console', 'file']
    )
    parser.add_argument(
        '--format',
        dest='format_report',
        help='Report output format.'
        'Possible value: json - save report in json format, '
             'csv - save report in csv format.',
        default='json',
        choices=['json', 'csv']
    )
    parser.add_argument(
        '--ext',
        dest='extension',
        default='py'

    )
    return parser.parse_args()


def statistic(project, top_size, part_of_speech, out_method, part_of_code, out_format):

    argspace = parse_args()

    trees = get_trees(project)
    if not trees:
        logging.info(
            'Could not create a tree, no files with extension "py" was found')
        return
    names_list = get_list_objects_name(trees, part_of_code)
    result_list = get_part_of_speech(names_list, part_of_speech)

    if str(out_method).lower() == 'file':
        output_format_choice(result_list, top_size, out_format, part_of_speech)
    else:
        output_console(result_list, top_size, part_of_speech)

    if argspace.repo_url:
        rm_dir(project)


def get_arg():
    argspace = parse_args()

    if argspace.dir_path:
        project = argspace.dir_path
    else:
        folder = mk_dir(argspace.repo_url)
        project = clone_repo(argspace.repo_url, folder)
        if not project:
            logging.info(
                'could not load repository by URL "{}"'.format(argspace.repo_url))
            rm_dir(folder)
            return

    if argspace.extension != 'py':
        logging.info(
            'This version of the project works only with files with the extension ".py"')
        return

    statistic(project, argspace.top_size, argspace.word_category,
                  argspace.output, argspace.names, argspace.format_report,)


if __name__ == '__main__':

    get_arg()
