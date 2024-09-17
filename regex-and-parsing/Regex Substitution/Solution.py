# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def process_text(n, lines):

    patterns = [
        (r"(?<= )&&(?= )", "and"),   
        (r"(?<= )\|\|(?= )", "or")   
    ]
    
   
    modified_lines = []
    for line in lines:
        modified_line = line
        for pattern, replacement in patterns:
            modified_line = re.sub(pattern, replacement, modified_line)
        modified_lines.append(modified_line)
    
    return modified_lines

n = int(input())
lines = [input() for _ in range(n)]


modified_lines = process_text(n, lines)
for line in modified_lines:
    print(line)
