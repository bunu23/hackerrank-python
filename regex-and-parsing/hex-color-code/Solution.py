# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = r"(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[;),])"

n = int(input())

print(*[color for line in (input() for _ in range(n)) for color in re.findall(pattern, line)], sep="\n")
