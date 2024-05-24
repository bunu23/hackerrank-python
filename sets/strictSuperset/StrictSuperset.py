# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))
n = int(input())
is_strict_superset = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    # Check if A is a strict superset of other_set
    if not (A > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)
