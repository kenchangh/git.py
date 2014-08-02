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
        self.remotes = self.get_remotes()
        shell.call('cd {repo}'.format(repo = repo))

    def init(self, options=''):
        options = parse_options(options)
        shell.call('git init {options}'.format(options = options))

    def get_remotes(self):
        try:
            remotes_dir = path.join(self.repo,
                                    '.git',
                                    'logs',
                                    'refs',
                                    'remotes')
            print remotes_dir                       
            return os.listdir(remotes_dir)
        except OSError:
            return False

    def check_is_bare(self):
        git_dir = path.join(self.repo, '.git')
        # Negate exists, is_bare means it does not exist.
        return not path.exists(git_dir)

    def add(self, files=[], options=''):
        options = parse_options(options)
        if files == []:
            shell.call('git add --all {options}'.format(
                       options = options))
        elif type(files) is list:
            files = ' '.join(files)
            shell.call('git add {options}'.format(
                       options = options) + files)
        else:
            raise TypeError('Files has to be list, not {0}'.format(
                            type_in_str(files)))

    def commit(self, files=[], message='', options=''):
        options = parse_options(options)
        message = '"-m {0} "'.format(message)
        if files == []:
            shell.call('git commit {options}{message}'.format(
                       options = options, message = message))
        elif type(files) is list:
            files = ' '.join(files)
            shell.call('git commit {options}{message}'.format(options = options) + files)
        else:
            raise TypeError('Files has to be in a list, not {0}'.format(
                            type_in_str(files)))


