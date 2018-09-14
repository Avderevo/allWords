import ast
import os

import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def get_filenames_list(path, ext='py'):
    for dirname, dirs, files in os.walk(path, topdown=False):
        for file in files:
            if file.endswith('.{}'.format(ext)):
                with open(os.path.join(dirname, file)) as filenames:
                    yield filenames.read()


def get_trees(path):
    trees = []
    for filename in get_filenames_list(path):
     
        try:

            tree = ast.parse(filename)

        except SyntaxError as e:
            logging.info(e)
            continue
        trees.append(tree)
    return trees
