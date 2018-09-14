from git import Repo, exc
from urllib import request
import urllib.error


import logging
logging.basicConfig(format=u' %(message)s', level=logging.INFO)


def clone_repo(git_url, folder):

    try:
        try:
            request.urlopen(git_url).getcode()
        except urllib.error.HTTPError:
            logging.info('Bad url "\033[33m{}\x1b[0m"'.format( git_url))
            return

        Repo.clone_from(git_url, folder)
  
    except exc.GitCommandError:
        logging.info('Repository {} does not exist'.format(git_url))

    return folder
