# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

def compress_string(s):
    # Using groupby to group consecutive identical characters
    groups = [(char, len(list(group))) for char, group in groupby(s)]
    
    # Formatting the result as required
    compressed_string = ' '.join(f"({count}, {char})" for char, count in groups)
    
    # Printing the result
    print(compressed_string)

# Sample Input
s = input().strip()
compress_string(s)
