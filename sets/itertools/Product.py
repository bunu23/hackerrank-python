# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product


A = list(map(int, input().split()))
B = list(map(int, input().split()))


cartesian_product = sorted(product(A, B))

for item in cartesian_product:
    print(item, end=' ')
