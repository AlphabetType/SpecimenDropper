# SpecimenDropper: Drop to InDesign

### What is it about?

With dropToInDesign you can automatically create multiple typeface specimens:
Drop one or more fonts onto the app. The script builds a specimen file for every font and opens it for you in InDesign.

* The fonts don’t have to be installed (at least if you use InDesign CS5 or later).
* You can edit the InDesign Template for your needs to create your own branded specimens.

### The specimen template

* You find the template file inside the app (Right click on the app, Show package contents: Contents -> Resources -> template_specimen.idml)
* You can add custom placeholder-variables in your template. (See dev notes below)
* You can duplicate the app, rename it and edit every template specimen for certain needs.
* Please keep in mind: Currently you have to assign a non-standard font with a style other than regular to a textbox (story) in InDesign. Otherwise the box won’t be recognized (and replaced with your dropped font).

### Any ideas?
This is currently the first version. If you have feature requests, just drop us a line!

### Dependencies
* Adobe InDesign CS5+
* MacOSX (If you want to use the standalone version of SpecimenDropper)

## Dev notes
If you want to have more control (like adding placeholder-variables), you should work with the uncompiled version. You can run the script via commandline and add one or more fonts as attributes. Example:

    python dropToInDesign.py user/test/desktop/FiraSans-Bold.otf user/test/desktop/FiraSans-Bold.otf

### Placeholder Variables
With variables you can add dynamic content to your template specimens.

These are the preset variables in your template:

* `{{timestamp}}` -> Current date and time 
* `{{familyname}}` -> Name of the font family
* `{{style}}` -> Name of the font style
* `{{filename}}` -> Filename of the font
* `{{headline}}` -> "alphabet-type.com"

You can add custom variables in `dropToInDesign.py` inside the placeholders dictionary. See the code-comments for further information.

## Development Dependencies
* fontTools (Get it here: https://github.com/behdad/fonttools/)
