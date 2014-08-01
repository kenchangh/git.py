##########

import os
import re
import shell
from os import path

##########

class TypeError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


def type_in_str(object_):
    with_type = str(type(object_)) 
    # Return string between single quote
    match = re.findall("'([^']*)'", with_type)
    # Only one match in list
    return match[0]

def parse_options(options):
    # Change ['-m', '-f']
    # To '-m -f '
    if type(options) is list:
        options = ' '.join(options) + ' '
    # Trailing space to split commands
    elif type(options) is str:
        options = options + ' '
    return options


class Repo(object):

    def __init__(self, repo=os.getcwd()):
        self.repo = repo
        self.is_bare = self.check_is_bare()
        shell.call('cd {repo}'.format(repo = repo))

    def init(self, options=''):
        options = parse_options(options)
        shell.call('git init {options}'.format(options = options))

    def check_is_bare():
        git_dir = path.join(self.repo, '.git')
        return path.exists(git_dir)

    def add(self, files=[], options=''):
        options = parse_options(options)
        if files == []:
            shell.call('git add --all {options}:/'.format(
                       options = options))
        elif type(files) is list:
            files = ' '.join(files)
            shell.call('git add {options}'.format(options = options) + files)
        else:
            raise TypeError('Files has to be list, not {0}'.format(
                            type_in_str(files)))

