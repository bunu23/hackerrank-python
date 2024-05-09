# Enter your code here. Read input from STDIN. Print output to STDOUT
size_a = int(input())
set_a = set(map(int, input().split()))
size_b = int(input())
set_b = set(map(int, input().split()))

symmetric_diff = set_a.symmetric_difference(set_b)

sorted_diff = sorted(symmetric_diff)

for num in sorted_diff:
    print(num)
