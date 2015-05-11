import os
import sys

def getInputpaths(debug=False):
    if debug:
        # If you use windows, you should use a windows compatible path
        return [os.path.join(os.path.expanduser('~'), 'Desktop')]

    elif len(sys.argv[1:]) > 0:
        return sys.argv[1:]
    else:
        print 'Please add a path as argument when running the script.'
        return False


if __name__ == '__main__':
    input_paths = getInputpaths(debug=True)
    if input_paths:
        print os.listdir(input_paths)