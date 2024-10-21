# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def parse_html(n, lines):
    html = "\n".join(lines)

    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    

    tag_pattern = r'<\s*([a-zA-Z0-9]+)'  
    attr_pattern = r'([a-zA-Z0-9\-]+)\s*=\s*"([^"]*)"'  
    
    # Iterate through the HTML lines
    for tag_match in re.finditer(tag_pattern, html):
        tag = tag_match.group(1) 
        
     
        tag_start = tag_match.start()
        tag_end = html.find('>', tag_start)
        if tag_end != -1:
            tag_content = html[tag_start:tag_end]  
            

            for attr_match in re.findall(attr_pattern, tag_content):
                attr, value = attr_match
                print(f"-> {attr} > {value}")

n = int(input())  
lines = [input().strip() for _ in range(n)]  


parse_html(n, lines)
