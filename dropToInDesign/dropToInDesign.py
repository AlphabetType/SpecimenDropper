import subprocess
import sys

def getInputpaths():
    arguments = []
    for f in sys.argv[1:]:
        arguments.append(f)

    return arguments

class CreateInDesignSpecimen:
    def __init__(self, path_list):
        print path_list
        self.path = False # set to false for dev reasons

        # Receive one or more fonts.

        # Copy every font into the document-fonts folder of a predefined directory

        # Read font data

        # Add all data to template InDesign file. (Create a page for every font.)


if __name__ == '__main__':
    input_paths = getInputpaths()
    specimen = CreateInDesignSpecimen(input_paths)

    # Open Specimen-file
    if specimen.path:
        subprocess.call(('open', specimen.path))

