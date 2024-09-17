# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def is_valid_mobile_number(number):
  
    pattern = r'^[789]\d{9}$'
    return re.match(pattern, number)


n = int(input())

for _ in range(n):
    mobile_number = input().strip()
    

    if is_valid_mobile_number(mobile_number):
        print("YES")
    else:
        print("NO")
