# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def is_valid_uid(uid):
   
    if len(uid) != 10:
        return False
    
    if not uid.isalnum():
        return False
  
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
   
    if len(re.findall(r'\d', uid)) < 3:
        return False
 
    if len(set(uid)) != 10:
        return False
    return True


num_cases = int(input().strip())
results = []

for _ in range(num_cases):
    uid = input().strip()
    if is_valid_uid(uid):
        results.append("Valid")
    else:
        results.append("Invalid")


for result in results:
    print(result)
