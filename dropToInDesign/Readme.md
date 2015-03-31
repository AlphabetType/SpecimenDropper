# Drop to InDesign

## What is it about?

With DropToInDesign you can automatically create multiple typeface specimens:
Drop one or more fonts onto the app and the script builds a specimen-file for every font and opens it for you in InDesign.

The fonts don’t have to be installed (at least if you use InDesign CS5 or later).

## The specimen template

* You the template file inside the app (Right click on the app, Show package contents -> Resources -> template_specimen.idml) as you wish.
* You can add custom placeholder-variables in your template. (See dev notes below)
* You can duplicate the app, rename it and edit every template specimen for certain needs.

## Any ideas?
This is currently the first version. If you have feature request, just drop us a line!

### Dependencies
* MacOSX
* Adobe InDesign CS5+

## Dev notes
If you want to have more control (like adding placeholder-variables), you should work with uncompiled version. You can run the script via commandline and add one or more fonts as attributes:

'''python dropToInDesign.py user/test/desktop/FiraSans-Bold.otf user/test/desktop/FiraSans-Bold.otf'''

## Development Dependencies
* fontTools (Get it here: https://github.com/behdad/fonttools/)