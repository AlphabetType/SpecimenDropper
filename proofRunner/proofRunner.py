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
        proof_path = os.path.join(self.rootPath, 'proof_' + filetype + '.html')
        try:
            with open(proof_path, 'w+') as proof_file:
                print 'Creating proof for %s files:\t %s' % (filetype, proof_path)
        except:
            print 'Error: Unable to create proof:\t %s' % proof_path



if __name__ == '__main__':
    input_paths = getInputpaths(debug=True)
    if input_paths:
        for path in input_paths:
            ProofRunner(path)