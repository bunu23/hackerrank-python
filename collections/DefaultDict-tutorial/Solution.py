# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]


indices = defaultdict(list)

for i in range(n):
    indices[group_a[i]].append(i + 1)


for word in group_b:
    if word in indices:
        print(" ".join(map(str, indices[word])))
    else:
        print(-1)
