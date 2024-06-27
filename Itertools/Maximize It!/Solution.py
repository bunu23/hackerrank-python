# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

def maximize_modulo(k, m, lists):
 
    all_combinations = product(*lists)
    
    max_value = 0
    for combination in all_combinations:
        # Calculate the sum of squares mod m
        current_value = sum(x ** 2 for x in combination) % m
        # Update max_value if current_value is greater
        if current_value > max_value:
            max_value = current_value
    
    return max_value


k, m = map(int, input().split())
lists = []
for _ in range(k):
    lists.append(list(map(int, input().split()))[1:])  # Skip the first number as it's just the count


print(maximize_modulo(k, m, lists))
