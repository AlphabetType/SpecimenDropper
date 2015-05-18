# SpecimenDropper: proofRunner

![proofRunner Example](https://github.com/AlphabetType/SpecimenDropper/blob/master/proofRunner/documentation_files/proofRunner_example.png)

### What is it about?
proofRunner creates an HTML page that displays all fonts inside a directory (and it’s subdirectories). This way you can easily spot erroneous fontfiles and collect them in a list to investigate them further.

### How does it work?
* Add one or more folders as arguments to the proofRunner script via commandline.
* proofRunner scans the folders and subfolder for fonts …
* … and creates one HTML file for all fonts of a specific fontformat in the root of the folder.
* The fonts are displayed via @font-face in the HTML file (The fonts are NOT moved. They get referenced with their specific location).
* Click on the fontbox to add the font path to a textbox at the end of the file.

### Customization
Take a look at `proofRunnerTemplate.py`. There you can edit the example string, the HTML markup, JavaScript and CSS styling. You can also add further filetypes (with their @font-face statement). TTF, OTF, EOT and WOFF are already predefined.

### Any ideas?
This is currently the first version. If you have feature requests, just drop us a line!

### Known Issues
* Obviously the browser you view the HTML file in must support the @font-face statement and the fontformat
* … though Firefox has a problem with the local URL in the @font-face statement and won’t display the fonts
