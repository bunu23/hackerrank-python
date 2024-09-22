# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            attr_name = attr[0]
            attr_value = attr[1] if attr[1] is not None else "None"
            print(f"-> {attr_name} > {attr_value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            attr_name = attr[0]
            attr_value = attr[1] if attr[1] is not None else "None"
            print(f"-> {attr_name} > {attr_value}")


n = int(input())  
html_code = ""
for _ in range(n):
    html_code += input()

parser = MyHTMLParser()
parser.feed(html_code)
