import os
import sys
import proofRunnerTemplate as template

def getInputpaths(debug=False):
    if debug:
        # If you use windows, you should use a windows compatible path
        return [os.path.join(os.path.expanduser('~'), 'Desktop')]

    elif len(sys.argv[1:]) > 0:
        return sys.argv[1:]
    else:
        print 'Please add a path as argument when running the script.'
        return False


class ProofRunner(object):
    def __init__(self, rootPath):
        self.rootPath = rootPath

        for extension in template.ff_statements:
            self.createProof(extension)

    def createProof(self, filetype):
        print 'Creating proof for %s files' % filetype


if __name__ == '__main__':
    input_paths = getInputpaths(debug=True)
    if input_paths:
        for path in input_paths:
            ProofRunner(path)