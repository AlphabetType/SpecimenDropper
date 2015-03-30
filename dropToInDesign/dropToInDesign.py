import subprocess
import sys, os

class ConfigData:
    def __init__(self):
        # Allowed filetypes must start with a dot
        self.allowedFiletypes = ['.otf', '.ttf']

def getInputpaths():
    arguments = []
    for f in sys.argv[1:]:
        arguments.append(f)

    return arguments

class CreateInDesignSpecimen:
    def __init__(self, path_list):
        self.path = False # set to false for dev reasons

        # Get config data
        self.c = ConfigData()

        # Receive one or more fonts.
        fontpath_list = self.acceptOnlyAllowedFiletypesInList(path_list)
        print fontpath_list

        # Copy every font into the document-fonts folder of a predefined directory

        # Read font data

        # Add all data to template InDesign file. (Create a page for every font.)

    def acceptOnlyAllowedFiletypesInList(self, pathlist_in):
        pathlist_out = []
        for p in pathlist_in:
            if os.path.splitext(p)[1] in self.c.allowedFiletypes:
                pathlist_out.append(p)
            else:
                print p, 'ignored, because it has no an allowed extension.'

        return pathlist_out



if __name__ == '__main__':
    input_paths = getInputpaths()
    specimen = CreateInDesignSpecimen(input_paths)

    # Open Specimen-file
    if specimen.path:
        subprocess.call(('open', specimen.path))

