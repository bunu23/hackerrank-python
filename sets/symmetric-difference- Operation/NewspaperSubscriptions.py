# Enter your code here. Read input from STDIN. Print output to STDOUT

n_english = int(input().strip())
english_subscribers = set(map(int, input().strip().split()))

n_french = int(input().strip())
french_subscribers = set(map(int, input().strip().split()))


symmetric_diff = english_subscribers.symmetric_difference(french_subscribers)


print(len(symmetric_diff))
