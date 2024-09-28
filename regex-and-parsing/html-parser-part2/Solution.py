from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_comment = False  
        self.multi_line_comment = []  

    def handle_comment(self, data):
        # Handle multi-line comments
        if '\n' in data:
            if self.multi_line_comment: 
                print(">>> Multi-line Comment")
                print("\n".join(self.multi_line_comment))
                self.multi_line_comment.clear()  
       
            print(">>> Multi-line Comment")
            print(data)
        else:
        
            if self.multi_line_comment:  
                print(">>> Multi-line Comment")
                print("\n".join(self.multi_line_comment))
                self.multi_line_comment.clear()  
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
     
        if data.strip():  
            print(">>> Data")
            print(data)

    def handle_endtag(self, tag):
     
        if tag == 'comment':
            if self.multi_line_comment:  # Print the stored multi-line comment
                print(">>> Multi-line Comment")
                print("\n".join(self.multi_line_comment))
                self.multi_line_comment.clear()  # Clear after printing


html = ""
for i in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
