# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def generate_combinations(s, k):
    s = sorted(s)  # Sort the string to ensure lexicographic order
    for i in range(1, k + 1):
        for combo in combinations(s, i):
            print(''.join(combo))

if __name__ == "__main__":
    # Read the input
    input_data = input().strip()
    s, k = input_data.split()
    k = int(k)
    # Call the function to generate and print combinations
    generate_combinations(s, k)
