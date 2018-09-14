from git import Repo, exc
from urllib import request


import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def clone_repo(git_url, folder):

    try:
        if str(request.urlopen(git_url).getcode()) == '200':

            Repo.clone_from(git_url, folder)

        else:
            logging.info('Bad status code url {}'.format(git_url))
            folder = None

    except exc.GitCommandError:
        logging.info('Repository {} does not exist'.format(git_url))
    return folder
