# Read input
a = int(input())
b = int(input())
m = int(input())

# Compute a^b
power_result = pow(a, b)

# Compute (a^b) % m
mod_power_result = pow(a, b, m)

# Print results
print(power_result)
print(mod_power_result)
