# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def comb(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def calculate_probability(n, letters, k):
    count_a = letters.count('a')
    count_not_a = n - count_a
    
    if k > n:
        return 0.0
    
    total_combinations = comb(n, k)
    if count_not_a >= k:
        no_a_combinations = comb(count_not_a, k)
    else:
        no_a_combinations = 0
    
    probability_no_a = no_a_combinations / total_combinations
    probability_at_least_one_a = 1 - probability_no_a
    
    return probability_at_least_one_a

# Reading input
n = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

# Calculate probability
result = calculate_probability(n, letters, k)

# Print result formatted to 4 decimal places
print(f"{result:.4f}")
