# file_handle = open("test.html", "w+b")
from TextClassificationEmotions import TextClassificationEmotions
import html

text_file = open('MobyDick.txt', 'r')
html_file = open("MobyDick.html", 'w+b')
style = """
body {
  background-color: white;
  font-family: 'Source Serif 4', serif;
  font-weight: normal;
  font-style: initial;
  color: black;
  margin-left: 10%;
  margin-right: 10%;
  # text-align: center; /* all headings centered */
  clear: both;
}
.pagenum { /* uncomment the next line for invisible page numbers */
    /*  visibility: hidden;  */
    position: absolute;
    left: 92%;
    font-size: smaller;
    text-align: right;
    font-style: normal;
    font-weight: normal;
    font-variant: normal;
} /* page numbers */


.blockquot {
    margin-left: 5%;
    margin-right: 10%;
}


.boxit{
    max-width: 14em;
    padding: 1em;
    border: 0.5em double black;
    margin: 0 auto; }

/*Indent-padding*/
.ir1{text-align:right; padding-right:1em}
.ir2{text-align:right; padding-right:2em}

.pminus1  {margin-top: -0.25em;}
.p1       {margin-top: 1em;}
.p2       {margin-top: 2em;}
.s1       {margin-bottom:-0.25em;}

div.chapter {page-break-before: always;}
.nobreak  {page-break-before: avoid; text-align: center;
           padding-top: 0;}
hr {
    width: 33%;
    margin-top: 2em;
    margin-bottom: 2em;
    margin-left: 33.5%;
    margin-right: 33.5%;
    clear: both;
}

h1 {
  margin-top: .51em;
  text-align: justify;
  margin-bottom: .49em;
  color: black;
  margin-left: 1px;
  font-family: 'Source Serif 4', serif;
  font-weight: bold;
  font-style: initial;
  font-size: xx-large;

}

p1 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: black;
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 400;
  letter-spacing: .1rem;
}

p2 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: rgba(0,0,0,0.87);
  font-family: 'Source Serif 4', serif;
  letter-spacing: 0;
}
p3 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: #340001;
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 900;
  font-style: initial;
}
p4 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: black;
  font-family: 'Source Serif 4', serif;
  font-style: italic;
  
}
p5 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: black;
  font-family: 'Source Sans 3', sans-serif;
  font-weight: 400;
  letter-spacing: 2;

}
p6 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: black;
  font-family: 'Source Serif 4', serif;
  font-weight: 300;
  letter-spacing: 2px;
  font-size: small;

}
p7 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: black;
  font-family: 'Source Sans 3', sans-serif;
  font-weight: normal;
}

p8 {
  margin-top: .51em;
  text-align:  left;
  margin-bottom: .49em;
  color: black;
  font-family: 'Source Serif 4', serif;
  font-weight: normal;
  font-style: initial;
}
"""

link = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&family=Source+Serif+Pro:ital,wght@0,200;0,300;0,400;0,600;0,700;0,900;1,200;1,300;1,400;1,600;1,700;1,900&display=swap" rel="stylesheet">"""
Lines = text_file.readlines()
cur_par = ""
t_c = TextClassificationEmotions()
# title = str(Lines[0].replace('Title:', ''))

html_text = "<!DOCTYPE html>\n<html>\n<head>"
html_text += link
html_text += "\n<style>"
html_text += style
html_text += "</style>\n</head>\n<body>"


def make_label(lable, text):
    return f'<{lable}>{text}</{lable}>\n<br><br>'


# Strips the newline character
def make_chapter(par):
    text = """<div class="chapter">\n<h2 class ="nobreak"> """
    text += par.replace("\"","&quot")
    text += """<br>
     </h2>\n</div>"""
    return text


counter = 0
for line in Lines:
    if line == '\n':
        if (cur_par.upper()) == cur_par:
            html_text += make_chapter(cur_par)

        else:
            try:
                pred = t_c.get_emotion_label(cur_par)
                html_text += make_label(pred, cur_par)
            except:
                print('no')
        cur_par = ""
    else:
        cur_par += line

text_file.close()
html_text += """</body>\n</html>\n"""
html_file.write(html_text.encode('ascii', 'xmlcharrefreplace'))
html_file.close()
