# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input = sys.stdin.read().strip()

try:
    result = eval(input)
    if result is not None:
        print(result)
except Exception as e:
    print("Error evaluating expression:", e)

