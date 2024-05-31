# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

# Read the input complex number
z = complex(input().strip())

# Calculate modulus (r)
r = abs(z)

# Calculate phase angle (theta)
theta = cmath.phase(z)

# Print results rounded to three decimal places
print(f"{r:.3f}")
print(f"{theta:.3f}")
