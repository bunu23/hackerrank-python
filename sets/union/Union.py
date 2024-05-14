# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

english_subs = set(map(int, input().split()))


m = int(input())

french_subs = set(map(int, input().split()))

total_subs = len(english_subs.union(french_subs))

print(total_subs)
