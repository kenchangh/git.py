import re
from shelldon import call as shell

class TypeError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

def type_str(object_):
    with_type = str(type(object_)) 
    # Return string between single quote
    match = re.findall("'([^']*)'", with_type)
    # Only one match in list
    return match[0]

class Repo(object):

    def __init__(self):
        pass

    def add(self, files = []):
        if files == []:
            shell('git add --all :/')
        elif type(files) is list:
            files = ' '.join(files)
            shell('git add ' + files)
        else:
            raise TypeError('Files has to be list, not {0}').format(
                            type_str(files))

