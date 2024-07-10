# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())


shoe_inventory = Counter(shoe_sizes)


total_earnings = 0

for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_inventory[size] > 0:
        total_earnings += price
        shoe_inventory[size] -= 1


print(total_earnings)
