import subprocess
import sys, os, shutil
import zipfile
from fontTools.ttLib import TTFont

class ConfigData:
    def __init__(self):
        # IDML template
        self.idml_template = os.path.join('dev', 'test_specimen.idml')

        # Placholders variables to replace
        self.placeholders = [
            {
                'id': 'fontname',
                'variable': '{{fontname}}',
                'replaceBy': 'test'
            }
        ]

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
        print sys.argv[0]

        # Get config data
        self.c = ConfigData()

        # Receive one or more fonts.
        self.fontpath_list = self.acceptOnlyAllowedFiletypesInList(path_list)

        # Copy every font into the document-fonts folder of a predefined directory
        self.copyFonts()

        # Read font data
        self.fontsdict = []
        for fontfile in self.fontpath_list:
            font = TTFont(fontfile)
            this_fontdict = {
                'fontpath': fontfile,
                'familyname': font['name'].getName(1,1,0).string,
                'style': font['name'].getName(2,1,0).string
            }
            self.fontsdict.append(this_fontdict)

        # Create a working directory from idml file
        #self.createTmpIDMLDir()

        # Add all data to template InDesign file. (Create a page for every font.)
        self.replaceIDContent()

        # Remove temporary dir
        #self.removeTmpIDMLDir()

    def definePlaceholders(self):
        raw_placeholders = self.c.placeholders


    def createTmpIDMLDir(self):
        os.mkdir('temp')

        # An IDML file is practically a zip file. So we can unzip it to our temp directory.
        with zipfile.ZipFile(self.c.idml_template) as zipped_idml:
            zipped_idml.extractall('temp')

    def removeTmpIDMLDir(self):
        shutil.rmtree('temp')

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


    def replaceIDContent(self):

        # Overwrite fonts.xml
        font_xml_file_content_old = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><idPkg:Fonts xmlns:idPkg="http://ns.adobe.com/AdobeInDesign/idml/1.0/packaging" DOMVersion="8.0">{{fontfamilylist}}</idPkg:Fonts>'

        for fontdata in self.fontsdict:
            print fontdata

        # Get all textboxes of idml document
        storyfolder = os.path.join('temp', 'Stories')

        for story_file in os.listdir(storyfolder):
            story_path = os.path.join(storyfolder, story_file)
            content_out = False

            # Open every story file and check if there is something to be replaced
            with open(story_path, 'r') as content_in:
                content = content_in.read()
                for placeholder in self.c.placeholders:
                    if placeholder['variable'] in content:
                        content_out = str(content)
                        content_out = content_out.replace(placeholder['variable'], placeholder['replaceBy'])

            # Save file with replaced content, if something was found
            if content_out:
                with open(story_path, 'w') as f:
                    f.write(content_out)


if __name__ == '__main__':
    input_paths = getInputpaths()
    specimen = CreateInDesignSpecimen(input_paths)

    # Open Specimen-file
    if specimen.path:
        subprocess.call(('open', specimen.path))

