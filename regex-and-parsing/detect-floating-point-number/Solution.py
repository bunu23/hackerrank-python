import re


def is_float_number(s):
   
    float_regex = r'^[+-]?(\d*\.\d+|\d+\.\d*)$'
    
    
    return bool(re.match(float_regex, s))

n = int(input().strip())


for _ in range(n):
   
    s = input().strip()

    print(is_float_number(s))
