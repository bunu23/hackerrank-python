# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


main_string = input().strip()
substring = input().strip()

found_match = False

start = 0
while True:

    match = re.search(substring, main_string[start:])
    
    if not match:
        break
    

    found_match = True
    start_index = start + match.start()
    end_index = start + match.end() - 1
    print(f"({start_index}, {end_index})")
    

    start += match.start() + 1


if not found_match:
    print("(-1, -1)")
