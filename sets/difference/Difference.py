# Enter your code here. Read input from STDIN. Print output to STDOUT

num_english_subscribers = int(input())
english_subscribers = set(map(int, input().split()))
num_french_subscribers = int(input())
french_subscribers = set(map(int, input().split()))

# Calculate the difference
only_english_subscribers = english_subscribers.difference(french_subscribers)

# Output the result
print(len(only_english_subscribers))
