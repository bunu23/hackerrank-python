# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

def main():
    import sys
    input = sys.stdin.read().strip()
    s, r = input.split()
    r = int(r)
    
    # Generate combinations with replacement and collect them
    combs = list(combinations_with_replacement(sorted(s), r))
    
    # Print each combination
    for comb in combs:
        print(''.join(comb))

if __name__ == "__main__":
    main()
