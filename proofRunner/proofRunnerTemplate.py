

# Add extension and their according @font-face-statement to this dictionary.
# Only filetypes which are in this dictionary are recognized by the proofRunner.
ff_statements = {
    'eot': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}"); src: url("{{filepath_long}}?#iefix") format("embedded-opentype"); font-weight: normal; font-style: normal}</style>',
    'woff': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}") format("woff"); font-weight: normal; font-style: normal}</style>',
    'ttf': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}") format("truetype"); font-weight: normal; font-style: normal}</style>',
    'otf': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}") format("opentype"); font-weight: normal; font-style: normal}</style>'
}


# This is the text that will be displayed for every found font
example_string = 'Alphabetfoxjumpkicks'


# Replace the URL to jQuery with a link to a local jQuqery file if you want to use the click-functionality (see <script> below) offline
# Placeholders with double curly brackets will be replaced in the main script.
html_in = '''
<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>{{title}}</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    </head>
    <body>
        <h1>{{title}}</h1>
'''

html_out = '''
        <h2>Selected errors</h2>
        <textarea class="error_box"></textarea>
        <div class="stat">Nr. of Fonts: {{count}}<br> Nr. of selected Errors: <span class="js_errorCount">0</span></div>
    </body>
    </html>
'''

fontbox = '''
        <div class="fontbox" data-thisFont="{{filepath}}">
            <p class="filepath">{{filepath}}</p><p class="example_string" style="font-family:\'{{basename}}\'">%s</p>
        </div>
''' % example_string

js_main = '''
<script>
    var errorFontpaths = {}
    $(document).ready(function() {

        $(".fontbox").click(function() {
            if(!$(this).hasClass("error")) {
                // Add as error
                errorFontpaths[$(this).attr("data-thisFont")] = '';
                $(this).addClass("error")
            } else {
                // Remove from Errors
                $(this).removeClass("error")
                delete errorFontpaths[$(this).attr("data-thisFont")];
            }

            printErrors()
        });

        printErrors = function() {

            var content = ''
            var errorCount = 0
            jQuery.each(errorFontpaths, function(path) {
               console.log(path);
               content += path + "\\n";
               errorCount++
            });

            $(".error_box").val(content)
            $('.js_errorCount').text(errorCount)
        }

    });
</script>
'''

css_main = '''
<style>
    body {
        font-family: monospace;
        padding: 1em;
        width: 90%;
    }

    .fontbox {
        border-left: 1em solid LimeGreen;
        padding: 0 0 1em 1em;
        cursor: pointer;
    }

    .fontbox:hover, .error:hover {
        background-color: Moccasin;
        border-color: orange;
    }

    .fontbox:hover .filepath, .error:hover .filepath {
        color: orange;
    }

    .fontbox:active {
        transform: scale(0.99);
    }

    .error {
        background-color: LightPink;
        border-color: red;
    }

    .error .filepath {
            color: red;
        }

    .filepath {
        color: LimeGreen;
    }

    .example_string {
        font-size: 3em;
    }

    textarea.error_box {
      width: 100%;
      height: 30em;
      font-family: monospace;
      margin: 1em 0;
    }
</style>
'''

