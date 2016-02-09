#!/usr/bin/env python

from sys import argv

filename = argv[1]
docname = argv[2]

html_top = "<html><head>"
# stylings
font_family = "georgia"
color = "#676767"

h1_size = "24"
h2_size = "18"
p_size = "14"

html_style = """<style>
html, body {
    font-family: """ + font_family + """;
    color: """ + color + """;
    }
h1 {
    font-size: """ + h1_size + """;
    }
h2 {
    font-size: """ + h2_size + """;
    }
p {
    font-size: """ + p_size + """;
    }
</style>
</head>
<body>"""

html_end = "</body></html>"

def createParagraph(para_string):
    return("<p>"+para_string+"</p>")

def createH1(h1_string):
    return("<h1>"+h1_string+"</h1>")

def createH2(h2_string):
    return("<h2>"+h2_string+"</h2>")

html_string = html_top + html_style

md_file = open(filename, "r")

for line in md_file:
    if (line[0] == "#" and line[1] == "#"):
        new_h2 = createH2(line[2:])
        html_string = html_string + new_h2
    elif (line[0] == "#"):
        new_h1 = createH1(line[1:])
        html_string = html_string + new_h1
    else:
        new_p = createParagraph(line)
        html_string = html_string + new_p

md_file.close()

html_string = html_string + html_end

html_file = open(docname + ".html", "w")
html_file.write(html_string)
html_file.close()

print("Script ended.")
