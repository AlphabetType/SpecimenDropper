import sys

def getInputpaths():
    if len(sys.argv[1:]) > 0:
        return sys.argv[1:]
    else:
        print 'Please add a path as argument when running the script.'
        return False


if __name__ == '__main__':
    input_paths = getInputpaths()
    if input_paths:
        pass