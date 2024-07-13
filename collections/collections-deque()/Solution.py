# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys


n = int(input())
d = deque()


for _ in range(n):
    operation = input().split()
    method = operation[0]
    
    if method == "append":
        d.append(int(operation[1]))
    elif method == "appendleft":
        d.appendleft(int(operation[1]))
    elif method == "pop":
        d.pop()
    elif method == "popleft":
        d.popleft()


print(" ".join(map(str, d)))
