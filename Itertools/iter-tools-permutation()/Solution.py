# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

def generate_permutations(s, r):

    perm = permutations(s, r)

    sorted_perm = sorted(perm)

    for p in sorted_perm:
        print(''.join(p))

if __name__ == "__main__":

    input_data = input().strip()
    s, r = input_data.split()
    r = int(r)

    generate_permutations(s, r)
