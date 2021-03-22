import bs4
import sys

for a in sys.argv[1:] :
    print(a)
    with open(a.replace(".html", ".txt"), "w") as out:
        txt = bs4.BeautifulSoup(open(a), from_encoding='cp1252').find("pre").text
        out.write(txt)
