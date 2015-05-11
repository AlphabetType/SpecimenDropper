

# Add extension and their according @font-face-statement to this dictionary.
# Only filetypes which are in this dictionary are recognized by the proofRunner.

ff_statements = {
    'eot': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}"); src: url("{{filepath_long}}?#iefix") format("embedded-opentype"); font-weight: normal; font-style: normal}</style>',
    'woff': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}") format("woff"); font-weight: normal; font-style: normal}</style>',
    'ttf': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}") format("truetype"); font-weight: normal; font-style: normal}</style>',
    'svg': '<style>@font-face { font-family: "{{basename}}"; src: url("{{filepath_long}}#{{basename}}") format("svg"); font-weight: normal; font-style: normal}</style>',
}