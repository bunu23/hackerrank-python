# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    T = int(data[0])
    patterns = data[1:T+1]
    
    for pattern in patterns:
        if is_valid_regex(pattern):
            print("True")
        else:
            print("False")

if __name__ == "__main__":
    main()
