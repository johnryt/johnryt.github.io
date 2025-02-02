import pandas as pd
import os
import sys

if len(sys.argv)>1:
    path = sys.argv[1]
else:
    path = "posters.tsv"

posters = pd.read_csv(path, sep="\t", header=0).dropna(how='all')

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"

loc_dict = {}

for row, item in posters.iterrows():

    md_filename = str(item.date) + "-" + str(item.url_slug) + ".md"
    html_filename = str(item.date) + "-" + str(item.url_slug)
    year = item.date[:4]

    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: posters" + "\n"

    #if len(str(item.type)) > 3:
        #md += 'type: "' + item.type + '"\n'
    #else:
    md += 'type: "Poster"\n'

    md += "permalink: /posters/" + html_filename + "\n"

    if len(str(item.venue)) > 3:
        md += 'venue: "' + item.venue + '"\n'

    if len(str(item.date)) > 3:
        md += "date: " + str(item.date) + "\n"

    if len(str(item.location)) > 3:
        md += 'location: "' + str(item.location) + '"\n'

    if len(str(item.poster_url)) > 3:
        md += "poster_url: " + item.poster_url + "\n"

    md += "---\n"

    if len(str(item.description)) > 3:
        md += "\n" + html_escape(item.description)

    if len(str(item.poster_url)) > 3:
        md += " Click title to download PDF.\n"
    else:
        md += "\n"


    md_filename = os.path.basename(md_filename)
    #print(md)

    with open("../_posters/" + md_filename, 'w') as f:
        f.write(md)


# These files are in the talks directory, one directory below where we're working from.
