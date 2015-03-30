import subprocess
import sys, os, shutil

class ConfigData:
    def __init__(self):
        # Allowed filetypes must start with a dot
        self.allowedFiletypes = ['.otf', '.ttf']

        # At the moment the fonts will be copied to a directory, relative to the script
        self.id_fonts_folderpath = os.path.join('specimen', 'Document fonts')

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
        self.fontpath_list = self.acceptOnlyAllowedFiletypesInList(path_list)

        # Copy every font into the document-fonts folder of a predefined directory
        self.copyFonts()

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

    def copyFonts(self):
        try:
            # Remove folder to have a clear start
            shutil.rmtree(self.c.id_fonts_folderpath)
        except:
            # Folder does not exist yet
            pass
        finally:
            # Create folder (again)
            os.mkdir(self.c.id_fonts_folderpath)

            # Copy fonts into empty folder
            for fontpath in self.fontpath_list:
                try:
                    shutil.copy(fontpath, self.c.id_fonts_folderpath)
                except:
                    print 'Error while copying', fontpath, 'to', self.c.id_fonts_folderpath



if __name__ == '__main__':
    input_paths = getInputpaths()
    specimen = CreateInDesignSpecimen(input_paths)

    # Open Specimen-file
    if specimen.path:
        subprocess.call(('open', specimen.path))

